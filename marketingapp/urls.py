from marketingapp.views import (
    AboutUsListAPIView,
    ContactUsCreateAPIView,
    CouponCodeListAPIView,
    FAQListAPIView,
    NewsletterCreateAPIView,
    PrivacyPolicyListAPIView,
    SocialMediaListAPIView,
    TermsAndConditionListAPIView,
)
from django.urls import path

urlpatterns = [
    path('about-us/', AboutUsListAPIView.as_view(), name='about-us'),
    path('contact-us/', ContactUsCreateAPIView.as_view(), name='contact-us'),
    path('coupon-code/', CouponCodeListAPIView.as_view(), name='coupon-code'),
    path('faq/', FAQListAPIView.as_view(), name='faq'),
    path('newsletter/', NewsletterCreateAPIView.as_view(), name='newsletter'),
    path('privacy-policy/', PrivacyPolicyListAPIView.as_view(), name='privacy-policy'),
    path('social-media/', SocialMediaListAPIView.as_view(), name='social-media'),
    path('terms-and-condition/', TermsAndConditionListAPIView.as_view(), name='terms-and-condition'),
]
