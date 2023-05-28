from django.db import models
from utils.models_base import (TimeBaseModel, ImageBaseModel)


class Type(TimeBaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['name']


class TypeImage(ImageBaseModel):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.type.name

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = 'Type Image'
        verbose_name_plural = 'Type Images'
        ordering = ['type']


class Category(TimeBaseModel):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['type', 'name']


class CategoryImage(ImageBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = 'Category Image'
        verbose_name_plural = 'Category Images'
        ordering = ['category']


class Product(TimeBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + self.category.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['category', 'name']


class ProductImage(ImageBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ['product']


class ProductDetail(TimeBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product.name + ' - ' + self.name

    class Meta:
        verbose_name = 'Product Detail'
        verbose_name_plural = 'Product Details'
        ordering = ['product', 'name']
        unique_together = ('product', 'name')


class Banner(TimeBaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banner_images')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['name']
