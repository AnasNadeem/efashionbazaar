from django.contrib import admin
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


class TimeBaseModelAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'created', 'updated')
    list_filter = ('is_active', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    list_editable = ('is_active',)


class AboutUsAdmin(TimeBaseModelAdmin):
    list_display = ('title', 'description',) + TimeBaseModelAdmin.list_display
    search_fields = ('title',)


class ContactUsAdmin(TimeBaseModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'subject',) + TimeBaseModelAdmin.list_display
    search_fields = ('name', 'email', 'phone_number', 'subject', 'message',)


class CouponCodeAdmin(TimeBaseModelAdmin):
    list_display = ('code', 'discount',) + TimeBaseModelAdmin.list_display
    search_fields = ('code',)


class FAQAdmin(TimeBaseModelAdmin):
    list_display = ('question',) + TimeBaseModelAdmin.list_display
    search_fields = ('question',)
    ordering = ('-created',)


class NewsletterAdmin(TimeBaseModelAdmin):
    list_display = ('email', 'phone_number',) + TimeBaseModelAdmin.list_display
    search_fields = ('email', 'phone_number',)
    ordering = ('-created',)


class PrivacyPolicyAdmin(TimeBaseModelAdmin):
    list_display = ('title', 'description',) + TimeBaseModelAdmin.list_display
    search_fields = ('title',)


class SocialMediaAdmin(TimeBaseModelAdmin):
    list_display = ('name', 'url',) + TimeBaseModelAdmin.list_display
    search_fields = ('name', 'url',)


class TermsAndConditionAdmin(TimeBaseModelAdmin):
    list_display = ('title', 'description',) + TimeBaseModelAdmin.list_display
    search_fields = ('title',)


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(CouponCode, CouponCodeAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(TermsAndCondition, TermsAndConditionAdmin)
