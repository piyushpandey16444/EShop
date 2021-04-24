from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Category(models.Model):
    name = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Product(models.Model):
    category = models.ForeignKey(
        "store.Category", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='uploads/products/')
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_category(category_name=None):
        if category_name:
            return Product.objects.filter(category__name=category_name)
        else:
            return Product.objects.all()
