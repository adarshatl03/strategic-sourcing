from django.shortcuts import render
from store.models import Product,Category
from store.serializers import ProductSerializer,CategorySerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.


from rest_framework import generics


class CategoryListAPIView(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[AllowAny]

class ProductListAPIView(generics.ListAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[AllowAny]

class ProductDetailAPIView(generics.RetrieveAPIView):
 
    serializer_class=ProductSerializer
    permission_classes=[AllowAny]

    def get_object(self):
        slug=self.kwargs["slug"]
        return Product.objects.get(slug=slug)