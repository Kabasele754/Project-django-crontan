from django.core.mail import send_mail
from .models import Notification
from django.conf import settings


def send_email_notifications():
    # Retrieve notifications to be sent via email
    notifications = Notification.objects.filter(sent=False)

    for notification in notifications:
        # Constructing the email body
        message = f"Dear user,\n\n{notification.content}\n\nSincerely,\nYour team {settings.SITE_NAME}"

        # Sending the email
        send_mail(
            subject=notification.subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[notification.recipient],
            fail_silently=False,
        )

        # Mark the notification as sent
        notification.sent = True
        notification.save()
