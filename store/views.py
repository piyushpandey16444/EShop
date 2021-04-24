from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Product, Category, CustomUser
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from .serializers import ProductSerializer, CategorySerializer
import json
from django.core.serializers.json import DjangoJSONEncoder
from .forms import UserAdminCreationForm, AuthenticateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
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


def signup_view(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            # here we can make is_active to false and make it true after email authentication
            form.save()

            # path to view
            # required domain
            # relative url for verification
            # encode uid
            # token

            uid64 = urlsafe_base64_encode(force_bytes(form.instance.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={
                "uid64": uid64,
                "token": token_generator.make_token(form),
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

        messages.add_message(request, messages.SUCCESS,
                             'Account is created, please verify your email.')
        return redirect('/signup/')
    return render(request, 'store/signup.html', {'form': form})


@receiver(post_save, sender=CustomUser)
def default_to_non_active(sender, instance, created, *args, **kwargs):
    if created:
        instance.is_active = False
        instance.save()


def login_view(request):
    form = AuthenticateForm()
    if request.method == "POST":
        auth_form = AuthenticateForm(request=request, data=request.POST)
        if auth_form.is_valid():
            email = auth_form.cleaned_data.get('username')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')

    return render(request, 'store/login.html', {'form': form})


def verification_view(request, uid64, token=None):
    return HttpResponseRedirect('/login/')
