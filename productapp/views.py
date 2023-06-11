from productapp.models import (
    # Attribute,
    Type,
    Category,
    Product,
    Banner,
)
from productapp.serializers import (
    # AttributeSerializer,
    TypeSerializer,
    CategorySerializer,
    CategoryInDepthSerializer,
    ProductSerializer,
    ProductInDepthSerializer,
    BannerSerializer,
    BannerInDepthSerializer,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


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


class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        category_serializer_map = {
            'retrieve': CategoryInDepthSerializer,
        }
        return category_serializer_map.get(self.action.lower(), CategorySerializer)


class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        product_serializer_map = {
            'retrieve': ProductInDepthSerializer,
        }
        return product_serializer_map.get(self.action.lower(), ProductSerializer)


class BannerViewSet(BaseModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get_serializer_class(self):
        banner_serializer_map = {
            'retrieve': BannerInDepthSerializer,
        }
        return banner_serializer_map.get(self.action.lower(), BannerSerializer)
