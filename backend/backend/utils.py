from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils import timezone 

def send_common_email(subject, recipient_email, context, template_name):

    # Render the email HTML content
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)

    try:
        # Send email using Django's send_mail
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_email,
            fail_silently=False,
            html_message=html_message,
        )
        email_sent_time = timezone.now()
        status_message = "Email sent successfully."
        email_status = "success"
    except Exception as e:
        email_sent_time = timezone.now()
        status_message = f"Failed to send email: {str(e)}"
        email_status = "failure"

    return {
        "message": status_message,
        "email_sent_time": email_sent_time,
        "status": email_status
    }
