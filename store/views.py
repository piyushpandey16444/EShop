from django.shortcuts import render, redirect
from .models import Product, Category, CustomUser
from django.http import JsonResponse, HttpResponseRedirect
from .forms import UserAdminCreationForm, AuthenticateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator


def compute_order(get_category=None, get_filter=None):
    if get_filter == 'l2h':
        product_objs = Product.get_product_by_category(
            category_name=get_category).order_by('price')
    else:
        product_objs = Product.get_product_by_category(
            category_name=get_category).order_by('-price')
    return product_objs


def home_view(request):
    if request.method == "GET" and request.is_ajax():
        get_category = request.GET.get('category_name', None)
        get_filter = request.GET.get('get_filter', None)
        product_objs = compute_order(
            get_category=get_category, get_filter=get_filter)
        return JsonResponse(data={'response': list(product_objs.values())}, safe=False)

    elif request.method == "GET":
        category_objs = Category.get_all_categories()
        get_category = request.GET.get('category_name', None)
        get_price = request.GET.get('price', None)
        if get_category:
            product_objs = Product.get_product_by_category(
                category_name=get_category)
        elif get_price:
            product_objs = compute_order(
                get_category=get_category, get_filter=get_price)
        else:
            product_objs = Product.get_product_by_category(
                category_name=None)

        context = {
            'products': product_objs,
            'categories': category_objs,
        }
        return render(request, 'store/home.html', context)


def sending_activation_email(request, form):
    uid64 = urlsafe_base64_encode(force_bytes(form.instance.pk))
    domain = get_current_site(request).domain
    link = reverse('activate', kwargs={
        "uid64": uid64,
        "token": token_generator.make_token(form.instance),
    })
    activate_url = f'http://{domain}{link}'

    email_body = f"Hi {form.instance.email}, \nPlease use this link to verify your account.\n {activate_url}"
    email_subject = "Activate your account."
    from_email = "mp_reply@botmail.com"
    to_email = [form.instance.email]
    email = EmailMessage(
        email_subject,
        email_body,
        from_email,
        to_email,
    )
    email.send(fail_silently=False)
    return True


def signup_view(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        password1 = form.data['password1']
        password2 = form.data['password2']
        email = form.data['email']
        if not email or not password1 or not password2:
            messages.error(request, 'Please provide all the fields.')
            return redirect('signup')
        if form.is_valid():
            form.save()
            mail_sent = sending_activation_email(request, form)
            if mail_sent:
                messages.success(request, 'Account is created, please verify your email.')
                return redirect('/signup/')
        else:
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, f"Declared email: {email} is not valid")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, f"Selected password is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request,
                                   f"Password and Confirmation Password do not match")
            return redirect('signup')
    return render(request, 'store/signup.html', {'form': form})


@receiver(post_save, sender=CustomUser)
def default_to_non_active(instance, created, **kwargs):
    if created:
        instance.is_active = False
        instance.save()


def login_view(request):
    form = AuthenticateForm()
    if request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                messages.success(request, 'Account is not active, please check your email.')
                return redirect('login')
            messages.error(request, 'Invalid credentials or account is not active, please check your email.')
            return redirect('login')
        messages.success(request, 'Please provide both the fields.')
        return redirect('login')
    return render(request, 'store/login.html', {'form': form})


def verification_view(request, uid64, token):
    """
    code for verification of token and activation of user based on token.
    """
    try:
        required_id = force_text(urlsafe_base64_decode(uid64))
        user = CustomUser.objects.get(id=required_id)

        if not token_generator.check_token(user, token):
            return redirect('login' + '?message=' + 'User already activated')
        if user.is_active:
            return redirect('login')
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully.')
        return redirect('login')

    except Exception as E:
        print("Exception: ", E)
    return HttpResponseRedirect('/login/')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')
