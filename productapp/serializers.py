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


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class TypeImageSerializer(ModelSerializer):
    class Meta:
        model = TypeImage
        fields = '__all__'


class TypeImageInDepthSerializer(ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = TypeImage
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryInDepthSerializer(ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = Category
        fields = '__all__'


class CategoryImageSerializer(ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'


class CategoryImageInDepthSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CategoryImage
        fields = '__all__'


class CategoryAttributeMapSerializer(ModelSerializer):
    class Meta:
        model = CategoryAttributeMap
        fields = '__all__'


class CategoryAttributeMapInDepthSerializer(ModelSerializer):
    category = CategorySerializer()
    attribute = AttributeSerializer()

    class Meta:
        model = CategoryAttributeMap
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductInDepthSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductImageInDepthSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductAttributeMapSerializer(ModelSerializer):
    class Meta:
        model = ProductAttributeMap
        fields = '__all__'


class ProductAttributeMapInDepthSerializer(ModelSerializer):
    product = ProductSerializer()
    attribute = AttributeSerializer()

    class Meta:
        model = ProductAttributeMap
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductDetailInDepthSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductEcommercePlatformSerializer(ModelSerializer):
    class Meta:
        model = ProductEcommercePlatform
        fields = '__all__'


class ProductEcommercePlatformInDepthSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductEcommercePlatform
        fields = '__all__'


class ProductFullInDepthSerializer(ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True, source='productimage_set')
    attributes = ProductAttributeMapSerializer(many=True, source='productattributemap_set')
    details = ProductDetailSerializer(many=True, source='productdetail_set')
    ecommerce_platforms = ProductEcommercePlatformSerializer(many=True, source='productecommerceplatform_set')

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'sku',
            'price',
            'quantity',
            'category',
            'description',
            'out_of_stock',
            'images',
            'attributes',
            'details',
            'ecommerce_platforms',
        )


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
