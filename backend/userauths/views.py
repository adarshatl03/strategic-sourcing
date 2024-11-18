from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics,permissions,response,status
from backend.utils import send_common_email
from userauths.models import User,Profile
from django.core.mail import send_mail
from django.utils import timezone 
from django.conf import settings
from userauths.serializers import CustomTokenObtainPairSerializer,RegisterSerilizer,UserSerializer
import random
import shortuuid
shortuuid.set_alphabet("0123456789")
# Create your views here.
class CustomTokenObtailPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerilizer

def generate_otp():
    uuid_key=shortuuid.uuid()
    unique_key=uuid_key[:6]
    return unique_key

class PasswordResetEmailVerify(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class=UserSerializer
    def get(self, request, *args, **kwargs):
     
        email = request.query_params.get("email")  # Extract email from query parameters

        if not email:
            return response.Response(
                {"message": "Email query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email=email).first()  # Using `filter` to avoid exceptions

        if user:
            user.otp = generate_otp()
            user.save()

            uidb64 = user.pk
            otp = user.otp

            # Construct the reset link
            link = f"http://localhost:5573/create-new-password?otp={otp}&uidb64={uidb64}"
            template_name="password_reset_email.html"
            context = {
            'reset_link': link,  # Activation link
            'current_year': timezone.now().year
        }
            # Email subject and message
            subject = "Password Reset Request"
            composer = send_common_email(subject,[user.email],context,template_name)
            success_message = "User created successfully."
            return response.Response({
            "message": success_message if composer["status"] == "success" else composer["message"],
            "email_sent_time": composer["email_sent_time"],
            "status": composer["status"]
        })
        else:
            return response.Response(
                {"message": "User with the provided email does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        
class PasswordChangeView(generics.CreateAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=UserSerializer

    def create(self,request,*args,**kwargs):
        payload = request.data

        otp=payload["otp"]
        uidb64=payload["uidb64"]

        password=payload["password"]

        user=User.objects.get(id=uidb64,otp=otp)

        if user:
            user.set_password(password)
            user.otp=None
            user.reset_tokken=None
            user.save()

            return response.Response({"message":"Password Changed Successfully"},status=status.HTTP_201_CREATED)
