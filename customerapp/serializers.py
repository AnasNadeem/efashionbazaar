from customerapp.models import (
    User,
    UserOTP,
    UserAddress,
    UserReview,
    UserWishlist,
    UserCart,
    UserOrder,
    UserOrderItem,
)
from productapp.serializers import ProductSerializer, ProductAttributeMapSerializer
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserOTPSerializer(ModelSerializer):
    class Meta:
        model = UserOTP
        fields = '__all__'


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class UserReviewSerializer(ModelSerializer):
    class Meta:
        model = UserReview
        fields = '__all__'


class UserInDetailSerializer(ModelSerializer):
    otp = UserOTPSerializer(source='userotp_set')
    addresses = UserAddressSerializer(many=True, source='useraddress_set')
    reviews = UserReviewSerializer(many=True, source='userreview_set')

    class Meta:
        model = User
        fields = '__all__'


class UserWishlistSerializer(ModelSerializer):
    class Meta:
        model = UserWishlist
        fields = '__all__'


class UserWishlistInDepthSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = UserWishlist
        fields = '__all__'


class UserCartSerializer(ModelSerializer):
    class Meta:
        model = UserCart
        fields = '__all__'


class UserCartInDepthSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = UserCart
        fields = '__all__'


class UserOrderItemSerializer(ModelSerializer):
    class Meta:
        model = UserOrderItem
        fields = '__all__'


class UserOrderItemInDepthSerializer(ModelSerializer):
    product = ProductSerializer()
    productattributemap = ProductAttributeMapSerializer()

    class Meta:
        model = UserOrderItem
        fields = '__all__'


class UserOrderSerializer(ModelSerializer):
    class Meta:
        model = UserOrder
        fields = '__all__'


class UserOrderInDepthSerializer(ModelSerializer):
    address = UserAddressSerializer()
    items = UserOrderItemSerializer(many=True, source='userorderitem_set')

    class Meta:
        model = UserOrder
        fields = '__all__'
