from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import time
# from django.template import loader


@shared_task
def send_email_task(subject, message, recipient_list):
    time.sleep(15) # for check celery
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list
    )
    # html_message = loader.render_to_string(
    #         'email_templates/email.html',
    #         {
    #             'user_name': 'adc',
    #             'subject':  'Thank you from',
    #         }
    #     )
    # send_mail(
    #     subject,
    #     message,
    #     settings.EMAIL_HOST_USER,
    #     recipient_list,
    #     fail_silently=True,
    #     html_message=html_message
    # )
    return None
