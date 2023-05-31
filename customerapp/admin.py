from django.contrib import admin
from customerapp.models import (
    User,
    UserOTP,
    UserAddress,
    UserWishlist,
    UserCart,
    UserOrder,
    UserOrderItem,
    UserReview,
)


class TimeBaseModelAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'created', 'updated')
    list_filter = ('is_active', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    list_editable = ('is_active',)


class UserWishlistInline(admin.TabularInline):
    model = UserWishlist
    extra = 0
    fk_name = 'user'


class UserAddressInline(admin.TabularInline):
    model = UserAddress
    extra = 0


class UserOTPInline(admin.TabularInline):
    model = UserOTP
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name', 'phone',)
    ordering = ('email',)
    inlines = (UserOTPInline, UserAddressInline, UserWishlistInline,)


class UserOTPAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'otp', 'is_verified',) + TimeBaseModelAdmin.list_display
    search_fields = ('user',)
    ordering = ('user',)
    fieldsets = (
        ('User OTP', {
            'fields': ('user', 'otp', 'is_verified')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class UserAddressAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'city', 'state', 'pincode', 'is_default',) + TimeBaseModelAdmin.list_display
    list_filter = ('is_default',) + TimeBaseModelAdmin.list_filter
    search_fields = ('user', 'city', 'state', 'pincode',)
    ordering = ('user',)
    fieldsets = (
        ('User Address', {
            'fields': ('user', 'address', 'city', 'state', 'pincode', 'phone_number', 'is_default')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class UserWishlistAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'product',) + TimeBaseModelAdmin.list_display
    search_fields = ('user__email', 'product__name', 'product__slug')
    ordering = ('user',)
    fieldsets = (
        ('User Wishlist', {
            'fields': ('user', 'product')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserOTP, UserOTPAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserWishlist, UserWishlistAdmin)
