from django.urls import include, path

urlpatterns = [
    path("auth/",include("userauths.urls")),
    path("store/",include("userauths.urls")),
    path("vendor/",include("userauths.urls")),
    path("customer/",include("userauths.urls")),

]
