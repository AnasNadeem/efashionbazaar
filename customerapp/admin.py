from django.contrib import admin
from customerapp.models import (
    User,
    UserOTP,
)


class TimeBaseModelAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'created', 'updated')
    list_filter = ('is_active', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    list_editable = ('is_active',)


class UserOTPInline(admin.TabularInline):
    model = UserOTP
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name', 'phone',)
    ordering = ('email',)
    inlines = (UserOTPInline,)


class UserOTPAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'otp', 'is_verified',) + TimeBaseModelAdmin.list_display
    search_fields = ('user',)
    ordering = ('user',)


admin.site.register(User, UserAdmin)
admin.site.register(UserOTP, UserOTPAdmin)
