from rest_framework import serializers

from store.models import Cart,Product,Gallery,Category,Specification,Size,Color,CartOrder,CartOrderItems,ProductFaq,Review,Wishlist,Coupens,Notification

from vendor.models import Vendor

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields="__all__"



class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields="__all__"


class SpecificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specification
        fields="__all__"


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields="__all__"


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True,read_only=True)
    color = ColorSerializer(many=True,read_only=True)
    Specification = SpecificationSerializer(many=True,read_only=True)
    size = SizeSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields=[
            "id",
            "title",
            "image",
            "description",
            "category",
            "price",
            "old_price",
            "shipping_amount",
            "stock_qty",
            "in_stock",
            "status",
            "featured",
            "views",
            "rating",
            "slug",
            "vendor",
            "gallery",
            "color",
            "Specification",
            "size",
            "pid",
            "date",
            "rating_count",
            ]
    def get_gallery(self, obj):
        # Call the gallery method from the model and serialize its result
        return GallerySerializer(obj.gallery(), many=True).data

    def get_color(self, obj):
        # Call the color method from the model and serialize its result
        return ColorSerializer(obj.color(), many=True).data

    def get_specification(self, obj):
        # Call the specification method from the model and serialize its result
        return SpecificationSerializer(obj.specification(), many=True).data

    def get_size(self, obj):
        # Call the size method from the model and serialize its result
        return SizeSerializer(obj.size(), many=True).data

    def get_rating_count(self, obj):
        # Call the rating_count method from the model
        return obj.rating_count()
    def __init__(self,*args,**kwargs):
            super(ProductSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3




class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(CartSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3




class CartOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartOrder
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(CartOrderSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3


class CartOrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartOrderItems
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(CartOrderItemSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3


class ProductFaqSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductFaq
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(ProductFaqSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3

class ProductReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(ProductReviewSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3


class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(VendorSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3


    
class WishlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wishlist
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(WishlistSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3

class CoupenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coupens
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(CoupenSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3

class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields="__all__"

    def __init__(self,*args,**kwargs):
            super(NotificationSerializer,self).__init__(*args,**kwargs)

            request = self.context.get("request")

            if request and request.method=="POST":
                self.Meta.depth = 0

            else:
                 self.Meta.depth = 3