from django.core.exceptions import ValidationError
from django.db import models

from utils.models_base import TimeBaseModel


class AboutUs(TimeBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        ordering = ['-created']


class ContactUs(TimeBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def clean(self):
        if not self.phone_number.startswith('+91'):
            raise ValidationError('Phone number should be Indian')

        if len(self.phone_number) != 13:
            raise ValidationError('Phone number should be 10 digits')

        if not self.phone_number[3:].isdigit():
            raise ValidationError('Phone number should be digits')

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
        ordering = ['-created']


class CouponCode(TimeBaseModel):
    code = models.CharField(max_length=15)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Coupon Code'
        verbose_name_plural = 'Coupon Codes'
        ordering = ['-created']
        unique_together = ('code', 'is_active')


class FAQ(TimeBaseModel):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-created']


class Newsletter(TimeBaseModel):
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.email} - {self.phone_number}'

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ['-created']


class PrivacyPolicy(TimeBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policies'
        ordering = ['-created']


class SocialMedia(TimeBaseModel):
    SOCIAL_MEDIA_CHOICES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('youtube', 'Youtube'),
    )

    name = models.CharField(max_length=50, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ['name']
        unique_together = ('name', 'url')


class TermsAndCondition(TimeBaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Terms And Condition'
        verbose_name_plural = 'Terms And Conditions'
        ordering = ['-created']
