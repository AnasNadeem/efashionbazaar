from django.contrib import admin
from productapp.models import (
    Banner,
    Type,
    TypeImage,
    Category,
    CategoryImage,
    Product,
    ProductImage,
    ProductDetail,
)


class TimeBaseModelAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'created', 'updated')
    list_filter = ('is_active', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    list_editable = ('is_active',)


class BannerAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'name', 'can_redirect', 'is_active', 'is_default',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'name')
    list_editable = ('is_default',) + TimeBaseModelAdmin.list_editable
    list_filter = ('is_default',) + TimeBaseModelAdmin.list_filter
    search_fields = ('name', 'description')
    fieldsets = (
        ('Banner', {
            'fields': ('name', 'description', 'image', 'is_active', 'is_default', 'can_redirect', 'type_redirect', 'category_redirect', 'product_redirect')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#inlinemodeladmin-options
class TypeImageInline(admin.TabularInline):
    model = TypeImage
    extra = 0


class TypeAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'name', 'slug', 'description',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'name')
    readonly_fields = ('slug',) + TimeBaseModelAdmin.readonly_fields
    search_fields = ('name', 'description')
    fieldsets = (
        ('Type', {
            'fields': ('name', 'slug', 'description', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )
    inlines = (TypeImageInline, )


class TypeImageAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'type', 'image_type', 'image', 'is_default',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'type')
    list_editable = ('is_default',) + TimeBaseModelAdmin.list_editable
    list_filter = ('is_default',) + TimeBaseModelAdmin.list_filter
    search_fields = ('type__name', 'image_type')
    fieldsets = (
        ('Type Image', {
            'fields': ('type', 'image_type', 'image', 'is_default')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1


class CategoryAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'type', 'name', 'slug', 'description',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'name')
    readonly_fields = ('slug',) + TimeBaseModelAdmin.readonly_fields
    list_filter = ('type',) + TimeBaseModelAdmin.list_filter
    search_fields = ('type__name', 'name', 'description')
    fieldsets = (
        ('Category', {
            'fields': ('type', 'name', 'slug', 'description', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )
    inlines = (CategoryImageInline, )


class CategoryImageAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'category', 'image_type', 'image', 'is_default',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'category')
    list_editable = ('is_default',) + TimeBaseModelAdmin.list_editable
    list_filter = ('is_default',) + TimeBaseModelAdmin.list_filter
    search_fields = ('category__name', 'image_type')
    fieldsets = (
        ('Category Image', {
            'fields': ('category', 'image_type', 'image', 'is_default')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 0


class ProductAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'category', 'name', 'slug', 'description', 'price',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'name')
    readonly_fields = ('slug',) + TimeBaseModelAdmin.readonly_fields
    list_filter = ('category',) + TimeBaseModelAdmin.list_filter
    search_fields = ('category__name', 'name', 'description', 'price')
    fieldsets = (
        ('Product', {
            'fields': ('category', 'name', 'slug', 'description', 'price', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )
    inlines = (ProductImageInline, ProductDetailInline,)


class ProductImageAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'product', 'image_type', 'image', 'is_default',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'product')
    list_editable = ('is_default',) + TimeBaseModelAdmin.list_editable
    list_filter = ('is_default',) + TimeBaseModelAdmin.list_filter
    search_fields = ('product__name', 'image_type')
    fieldsets = (
        ('Product Image', {
            'fields': ('product', 'image_type', 'image', 'is_default')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


class ProductDetailAdmin(TimeBaseModelAdmin):
    list_display = ('id', 'product', 'name', 'description',) + TimeBaseModelAdmin.list_display
    list_display_links = ('id', 'name')
    search_fields = ('product__name', 'name', 'description')
    fieldsets = (
        ('Product Detail', {
            'fields': ('product', 'name', 'description', 'is_active')
        }),
        ('Time', {
            'fields': ('created', 'updated')
        }),
    )


admin.site.register(Banner, BannerAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(TypeImage, TypeImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryImage, CategoryImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
