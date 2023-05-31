from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.models_base import TimeBaseModel
from productapp.models import Product, ProductAttributeMap


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
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

        if extra_fields.get('is_staff') is not False:
            raise ValueError('is_staff must be False')

        if extra_fields.get('is_superuser') is not False:
            raise ValueError('is_superuser must be False')

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # Django default fields
    username = None
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # Our Custom fields
    phone = models.CharField(max_length=15, blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserOTP(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - {self.is_verified}'

    class Meta:
        verbose_name = 'User OTP'
        verbose_name_plural = 'User OTPs'
        ordering = ['user']


class UserAddress(TimeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15, blank=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - {self.address}'

    class Meta:
        verbose_name = 'User Address'
        verbose_name_plural = 'User Addresses'
        ordering = ['user']


class UserReview(TimeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.email} - {self.product.name}'

    class Meta:
        verbose_name = 'User Review'
        verbose_name_plural = 'User Reviews'
        ordering = ['user']


class UserWishlist(TimeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} - {self.product.name}'

    class Meta:
        verbose_name = 'User Wishlist'
        verbose_name_plural = 'User Wishlists'
        ordering = ['user']
        unique_together = ('user', 'product')


class UserCart(TimeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user.email} - {self.product.name}'

    class Meta:
        verbose_name = 'User Cart'
        verbose_name_plural = 'User Carts'
        ordering = ['user']

    @property
    def total_amount(self):
        return self.quantity * self.product.price


class UserOrder(TimeBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    is_delivered = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} - {self.address}'

    class Meta:
        verbose_name = 'User Order'
        verbose_name_plural = 'User Orders'
        ordering = ['user']


class UserOrderItem(TimeBaseModel):
    userorder = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    productattributemap = models.ForeignKey(ProductAttributeMap, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.userorder.user.email} - {self.product.name}'

    class Meta:
        verbose_name = 'User Order Item'
        verbose_name_plural = 'User Order Items'
        ordering = ['userorder']

    @property
    def total_amount(self):
        return self.quantity * self.product.price
