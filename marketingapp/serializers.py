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
from rest_framework.serializers import ModelSerializer


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class CouponCodeSerializer(ModelSerializer):
    class Meta:
        model = CouponCode
        fields = '__all__'


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


class PrivacyPolicySerializer(ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class TermsAndConditionSerializer(ModelSerializer):
    class Meta:
        model = TermsAndCondition
        fields = '__all__'
