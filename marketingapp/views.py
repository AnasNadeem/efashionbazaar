from marketingapp.models import (
    AboutUs,
    ContactUs,
    CouponCode,
    FAQ,
    Newsletter,
    PrivacyPolicy,
    SocialMedia,
    TermsAndCondition,
)
from marketingapp.serializers import (
    AboutUsSerializer,
    ContactUsSerializer,
    CouponCodeSerializer,
    FAQSerializer,
    NewsletterSerializer,
    PrivacyPolicySerializer,
    SocialMediaSerializer,
    TermsAndConditionSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)


class AboutUsListAPIView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ContactUsCreateAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class CouponCodeListAPIView(ListAPIView):
    queryset = CouponCode.objects.all()
    serializer_class = CouponCodeSerializer


class FAQListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class NewsletterCreateAPIView(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class PrivacyPolicyListAPIView(ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class TermsAndConditionListAPIView(ListAPIView):
    queryset = TermsAndCondition.objects.all()
    serializer_class = TermsAndConditionSerializer
