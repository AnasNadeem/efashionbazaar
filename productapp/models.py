from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models

from autoslug import AutoSlugField
from utils.models_base import (TimeBaseModel, ImageBaseModel)


class Attribute(TimeBaseModel):
    """ For example: Size, Color, etc """
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        ordering = ['name']

    def __str__(self):
        return self.name


class Type(TimeBaseModel):
    """ For example: Men, Women, Kids etc """
    name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['name']

    def __str__(self):
        return self.name


class TypeImage(ImageBaseModel):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Type Image'
        verbose_name_plural = 'Type Images'

    def __str__(self):
        return self.type.name

    def clean(self):
        super().clean()


class Category(TimeBaseModel):
    """ For example: Men: Kurta, Women: Kurti, etc"""
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = ('type', 'name')

    def __str__(self):
        return self.name


class CategoryAttributeMap(TimeBaseModel):
    """For ex: Kurta: Size, Color, etc. This will use in filtering"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    values = ArrayField(models.CharField(max_length=50), blank=True, null=True)

    class Meta:
        verbose_name = 'Category Attribute Map'
        verbose_name_plural = 'Category Attribute Maps'
        unique_together = ('category', 'attribute')

    def __str__(self):
        return self.category.name + ' - ' + self.attribute.name


class CategoryImage(ImageBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category Image'
        verbose_name_plural = 'Category Images'
        ordering = ['category']

    def __str__(self):
        return self.category.name

    def clean(self):
        super().clean()


class Product(TimeBaseModel):
    """ For example: Kurta: Linen Kurta, Cotton Kurta, etc"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name', unique=True)
    sku = AutoSlugField(populate_from='generate_sku', unique=True, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    out_of_stock = models.BooleanField(default=False)
    # attr_value = models.ManyToManyField(AttributeValue, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        unique_together = ('category', 'name')

    @property
    def generate_sku(self):
        return self.category.slug + '-' + self.slug

    def __str__(self):
        return self.name + ' - ' + self.category.name


class ProductAttributeMap(TimeBaseModel):
    """ For example: Kurta Size: 10, Kurta Color: Red, etc """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=150)
    stock = models.IntegerField(default=0)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Attribute Map'
        verbose_name_plural = 'Product Attribute Maps'
        unique_together = ('attribute', 'value')

    def __str__(self):
        return self.attribute.name + ' - ' + self.value

    def clean(self):
        if self.stock > self.product.quantity:
            raise ValidationError('Stock cannot be greater than product quantity')
        super().clean()


class ProductImage(ImageBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name

    def clean(self):
        super().clean()


class ProductDetail(TimeBaseModel):
    """ For example: Is washable: True, Material: Cotton, etc """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = 'Product Detail'
        verbose_name_plural = 'Product Details'
        ordering = ['product', 'name']
        unique_together = ('product', 'name')

    def __str__(self):
        return self.product.name + ' - ' + self.name


class ProductEcommercePlatform(TimeBaseModel):
    """ For example: Amazon, Flipkart, etc """
    PLATFORM = (
        ('ajio', 'Ajio')
        ('amazon', 'Amazon'),
        ('flipkart', 'Flipkart'),
        ('meesho', 'Meesho'),
        ('myntra', 'Myntra'),
        ('nykaa', 'Nykaa'),
        ('tatacliq', 'Tata Cliq'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50, choices=PLATFORM)
    url = models.URLField()
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Ecommerce Platform'
        verbose_name_plural = 'Product Ecommerce Platforms'
        unique_together = ('product', 'platform')

    def __str__(self):
        return self.platform + ' - ' + self.product.name


class Banner(TimeBaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banner_images')
    is_default = models.BooleanField(default=False)
    can_redirect = models.BooleanField(default=False)
    type_redirect = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    category_redirect = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product_redirect = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.name

    def clean(self):
        if self.is_default:
            default_banner = Banner.objects.filter(is_default=True)
            if default_banner.exists():
                raise ValidationError('Default banner already exists')

        if self.can_redirect:
            if (not self.type_redirect) or (not self.category_redirect) or (not self.product_redirect):
                raise ValidationError('Please select a redirect option')

        super().clean()
