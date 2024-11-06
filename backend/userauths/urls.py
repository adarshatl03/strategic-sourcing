from django.urls import path
from userauths import views as userauth_views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("login/",userauth_views.CustomTokenObtailPairView.as_view()),
    path("register/",userauth_views.RegisterView.as_view()),
    path("refresh/",TokenRefreshView.as_view())
]
