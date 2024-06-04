from celery import shared_task
from django.core.mail import send_mail
from .models import Subscription
import datetime

@shared_task
def send_birthday_notifications():
    today = datetime.date.today()
    subscriptions = Subscription.objects.filter(employee__birthday=today, subscribed=True)
    for subscription in subscriptions:
        send_mail(
            'Happy Birthday!',
            f'Happy Birthday, {subscription.employee.user.first_name}!',
            'from@example.com',
            [subscription.user.email],
            fail_silently=False,
        )
