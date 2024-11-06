from django.urls import path
from userauths import views as userauth_views

urlpatterns = [
    path("login/",userauth_views.CustomTokenObtailPairView.as_view()),
    path("register/",userauth_views.RegisterView.as_view())
]
