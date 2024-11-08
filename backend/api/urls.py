from django.urls import include, path

urlpatterns = [
    path("auth/",include("userauths.urls")),


]
