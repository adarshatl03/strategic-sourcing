from django.urls import include, path
from store import views as store_view
urlpatterns = [
    path("category",store_view.CategoryListAPIView.as_view()),
    path("products",store_view.ProductListAPIView.as_view()),
    path("products/<slug>",store_view.ProductDetailAPIView.as_view()),
    path("cart",store_view.CartAPIView.as_view()),
    
    path("auth/",include("userauths.urls")),
   


]
