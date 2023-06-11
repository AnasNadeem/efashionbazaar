from productapp.views import (
    TypeViewSet,
    # TypeImageViewSet,
    CategoryViewSet,
    # CategoryImageViewSet,
    # CategoryAttributeMapViewSet,
    ProductViewSet,
    # ProductImageViewSet,
    # ProductAttributeMapViewSet,
    # ProductDetailViewSet,
    # ProductEcommercePlatformViewSet,
    BannerViewSet,
)
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'type', TypeViewSet, basename='type')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'banner', BannerViewSet, basename='banner')

urlpatterns = []

urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)
