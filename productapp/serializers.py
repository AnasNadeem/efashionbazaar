from productapp.models import (
    Attribute,
    Type,
    TypeImage,
    Category,
    CategoryImage,
    CategoryAttributeMap,
    Product,
    ProductImage,
    ProductAttributeMap,
    ProductDetail,
    ProductEcommercePlatform,
    Banner,
)
from rest_framework.serializers import ModelSerializer


class AttributeSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class TypeImageSerializer(ModelSerializer):
    class Meta:
        model = TypeImage
        fields = '__all__'


class TypeSerializer(ModelSerializer):
    images = TypeImageSerializer(many=True, source='typeimage_set')

    class Meta:
        model = Type
        fields = '__all__'


class CategoryImageSerializer(ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'


class CategoryAttributeMapSerializer(ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = CategoryAttributeMap
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    images = CategoryImageSerializer(many=True, source='categoryimage_set')
    attributemaps = CategoryAttributeMapSerializer(many=True, source='categoryattributemap_set')

    class Meta:
        model = Category
        fields = '__all__'


class CategoryInDepthSerializer(ModelSerializer):
    type = TypeSerializer()
    images = CategoryImageSerializer(many=True, source='categoryimage_set')
    attributemaps = CategoryAttributeMapSerializer(many=True, source='categoryattributemap_set')

    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductAttributeMapSerializer(ModelSerializer):
    class Meta:
        model = ProductAttributeMap
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductEcommercePlatformSerializer(ModelSerializer):
    class Meta:
        model = ProductEcommercePlatform
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, source='productimage_set')
    attributes = ProductAttributeMapSerializer(many=True, source='productattributemap_set')
    details = ProductDetailSerializer(many=True, source='productdetail_set')
    ecommerceplatforms = ProductEcommercePlatformSerializer(many=True, source='productecommerceplatform_set')

    class Meta:
        model = Product
        fields = '__all__'


class ProductInDepthSerializer(ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True, source='productimage_set')
    attributes = ProductAttributeMapSerializer(many=True, source='productattributemap_set')
    details = ProductDetailSerializer(many=True, source='productdetail_set')
    ecommerceplatforms = ProductEcommercePlatformSerializer(many=True, source='productecommerceplatform_set')

    class Meta:
        model = Product
        fields = '__all__'


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class BannerInDepthSerializer(ModelSerializer):
    type_redirect = TypeSerializer()
    category_redirect = CategorySerializer()
    product_redirect = ProductSerializer()

    class Meta:
        model = Banner
        fields = '__all__'
