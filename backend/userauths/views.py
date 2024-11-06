from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics,permissions,response,status
from userauths.models import User,Profile
from django.core.mail import send_mail
from django.utils import timezone 
from django.conf import settings
from userauths.serializer import CustomTokenObtainPairSerializer,RegisterSerilizer,UserSerializer
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

            uidb64 = user.id
            otp = user.otp

            # Construct the reset link
            link = f"http://localhost:5573/create-new-password?otp={otp}&uidb64={uidb64}"

            # Email subject and message
            subject = "Password Reset Request"
            message = f"Hello, \n\nYou requested to reset your password. Click the link below to reset it:\n\n{link}\n\nIf you did not request this, please ignore this email."

            try:
                # Send email and capture the result
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,  # The sender's email address
                    [email],  # List of recipient email addresses
                    fail_silently=False,
                )

                # Email sent time and status
                email_sent_time = timezone.now()
                status_message = "Password reset email sent successfully."
                email_status = "success"

            except Exception as e:
                # Capture any errors in sending the email
                email_sent_time = timezone.now()
                status_message = f"Failed to send email: {str(e)}"
                email_status = "failure"

            # Log the status (you could also save this info in the database if needed)
            print(f"Email Status: {email_status}")
            print(f"Email Sent Time: {email_sent_time}")
            print(f"Status Message: {status_message}")

            return response.Response(
                {"message": status_message, "email_sent_time": email_sent_time, "status": email_status},
                status=status.HTTP_200_OK
            )
        else:
            return response.Response(
                {"message": "User with the provided email does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )