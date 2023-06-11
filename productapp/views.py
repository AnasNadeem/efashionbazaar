from productapp.models import (
    # Attribute,
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
from productapp.serializers import (
    # AttributeSerializer,
    TypeSerializer,
    TypeImageSerializer,
    TypeImageInDepthSerializer,
    CategorySerializer,
    CategoryInDepthSerializer,
    CategoryImageSerializer,
    CategoryImageInDepthSerializer,
    CategoryAttributeMapSerializer,
    CategoryAttributeMapInDepthSerializer,
    ProductSerializer,
    ProductInDepthSerializer,
    ProductImageSerializer,
    ProductImageInDepthSerializer,
    ProductAttributeMapSerializer,
    ProductAttributeMapInDepthSerializer,
    ProductDetailSerializer,
    ProductDetailInDepthSerializer,
    ProductEcommercePlatformSerializer,
    ProductEcommercePlatformInDepthSerializer,
    ProductFullInDepthSerializer,
    BannerSerializer,
    BannerInDepthSerializer,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class BaseModelViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if self.action in ['list', 'retrieve']:
            queryset = queryset.filter(is_active=True)
        return queryset

    # Stop POST/PUT/PATCH/DELETE request
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TypeViewSet(BaseModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def get_serializer_class(self):
        type_serializer_map = {
            'retrieve': TypeImageInDepthSerializer,
        }
        return type_serializer_map.get(self.action.lower(), TypeSerializer)


class TypeImageViewSet(BaseModelViewSet):
    queryset = TypeImage.objects.all()
    serializer_class = TypeImageSerializer

    def get_serializer_class(self):
        typeimage_serializer_map = {
            'retrieve': TypeImageInDepthSerializer,
        }
        return typeimage_serializer_map.get(self.action.lower(), TypeImageSerializer)


class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        category_serializer_map = {
            'retrieve': CategoryInDepthSerializer,
        }
        return category_serializer_map.get(self.action.lower(), CategorySerializer)


class CategoryImageViewSet(BaseModelViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer

    def get_serializer_class(self):
        categoryimage_serializer_map = {
            'retrieve': CategoryImageInDepthSerializer,
        }
        return categoryimage_serializer_map.get(self.action.lower(), CategoryImageSerializer)


class CategoryAttributeMapViewSet(BaseModelViewSet):
    queryset = CategoryAttributeMap.objects.all()
    serializer_class = CategoryAttributeMapSerializer

    def get_serializer_class(self):
        categoryattributemap_serializer_map = {
            'retrieve': CategoryAttributeMapInDepthSerializer,
        }
        return categoryattributemap_serializer_map.get(self.action.lower(), CategoryAttributeMapSerializer)


class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        product_serializer_map = {
            'retrieve': ProductInDepthSerializer,
        }
        return product_serializer_map.get(self.action.lower(), ProductSerializer)

    @action(detail=True, methods=['get'])
    def full(self, request, pk=None):
        product = self.get_object()
        serializer = ProductFullInDepthSerializer(product)
        return Response(serializer.data)


class ProductImageViewSet(BaseModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_serializer_class(self):
        productimage_serializer_map = {
            'retrieve': ProductImageInDepthSerializer,
        }
        return productimage_serializer_map.get(self.action.lower(), ProductImageSerializer)


class ProductAttributeMapViewSet(BaseModelViewSet):
    queryset = ProductAttributeMap.objects.all()
    serializer_class = ProductAttributeMapSerializer

    def get_serializer_class(self):
        productattributemap_serializer_map = {
            'retrieve': ProductAttributeMapInDepthSerializer,
        }
        return productattributemap_serializer_map.get(self.action.lower(), ProductAttributeMapSerializer)


class ProductDetailViewSet(BaseModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

    def get_serializer_class(self):
        productdetail_serializer_map = {
            'retrieve': ProductDetailInDepthSerializer,
        }
        return productdetail_serializer_map.get(self.action.lower(), ProductDetailSerializer)


class ProductEcommercePlatformViewSet(BaseModelViewSet):
    queryset = ProductEcommercePlatform.objects.all()
    serializer_class = ProductEcommercePlatformSerializer

    def get_serializer_class(self):
        productecommerceplatform_serializer_map = {
            'retrieve': ProductEcommercePlatformInDepthSerializer,
        }
        return productecommerceplatform_serializer_map.get(self.action.lower(), ProductEcommercePlatformSerializer)


class BannerViewSet(BaseModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get_serializer_class(self):
        banner_serializer_map = {
            'retrieve': BannerInDepthSerializer,
        }
        return banner_serializer_map.get(self.action.lower(), BannerSerializer)
