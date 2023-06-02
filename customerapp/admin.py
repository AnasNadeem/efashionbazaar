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


class UserOrderInline(admin.TabularInline):
    model = UserOrder
    extra = 0
    fk_name = 'user'


class UserCartInline(admin.TabularInline):
    model = UserCart
    extra = 0
    fk_name = 'user'
    readonly_fields = ('total_amount',)
    fields = ('user', 'product', 'quantity', 'total_amount', 'is_active')


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
    list_display = ('email', 'first_name', 'last_name', 'phone', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name', 'phone',)
    ordering = ('-date_joined',)
    inlines = (UserOTPInline, UserAddressInline, UserWishlistInline, UserCartInline, UserOrderInline,)


class UserOTPAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'otp', 'is_verified',) + TimeBaseModelAdmin.list_display
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone',)
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
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone', 'city', 'state', 'pincode',)
    fieldsets = (
        ('User Address', {
            'fields': ('user', 'address', 'city', 'state', 'pincode', 'phone_number', 'is_default', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class UserReviewAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'product', 'rating',) + TimeBaseModelAdmin.list_display
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone', 'product__name', 'product__slug')
    fieldsets = (
        ('User Review', {
            'fields': ('user', 'product', 'rating', 'comment', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class UserWishlistAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'product',) + TimeBaseModelAdmin.list_display
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone', 'product__name', 'product__slug')
    fieldsets = (
        ('User Wishlist', {
            'fields': ('user', 'product', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class UserCartAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_amount') + TimeBaseModelAdmin.list_display
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone', 'product__name', 'product__slug')
    readonly_fields = ('total_amount',) + TimeBaseModelAdmin.readonly_fields
    fieldsets = (
        ('User Cart', {
            'fields': ('user', 'product', 'quantity', 'total_amount', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class UserOrderItemInline(admin.TabularInline):
    model = UserOrderItem
    extra = 0
    fk_name = 'userorder'
    readonly_fields = ('total_amount',)
    fields = ('product', 'productattributemap', 'quantity', 'total_amount', 'is_active')


class UserOrderAdmin(TimeBaseModelAdmin):
    list_display = ('user', 'total_amount', 'is_paid', 'is_delivered', 'is_cancelled',) + TimeBaseModelAdmin.list_display
    list_filter = ('is_paid', 'is_delivered', 'is_cancelled',) + TimeBaseModelAdmin.list_filter
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone', 'address__address', 'address__city', 'address__state', 'address__pincode')
    fieldsets = (
        ('User Order', {
            'fields': ('user', 'address', 'total_amount')
        }),
        ('Order Status', {
            'fields': ('is_paid', 'is_delivered', 'is_cancelled', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )
    inlines = (UserOrderItemInline,)


class UserOrderItemAdmin(TimeBaseModelAdmin):
    list_display = ('userorder', 'product', 'productattributemap', 'quantity', 'total_amount',) + TimeBaseModelAdmin.list_display
    search_fields = ('userorder__user__email', 'user__first_name', 'user__last_name', 'userorder__user__phone', 'productattributemap__attribute__name', 'productattributemap__value', 'product__name', 'product__slug',)
    readonly_fields = ('total_amount',) + TimeBaseModelAdmin.readonly_fields
    fieldsets = (
        ('User Order Item', {
            'fields': ('userorder', 'product', 'productattributemap', 'quantity', 'total_amount', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserOTP, UserOTPAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(UserWishlist, UserWishlistAdmin)
admin.site.register(UserCart, UserCartAdmin)
admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(UserOrderItem, UserOrderItemAdmin)
