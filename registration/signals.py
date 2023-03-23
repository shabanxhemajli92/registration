from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Registration
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Registration)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New registration created'
        message = f'A new registration has been created with the following details:\n\nFull Name: {instance.full_name}\nPhone Number: {instance.phone_number}\nID Number: {instance.id_number}'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL], fail_silently=True)
        logger.info(f"Registration email sent to {settings.ADMIN_EMAIL}")

post_save.connect(send_registration_email, sender=Registration)

@receiver(post_delete, sender=Registration)
def send_registration_delete_email(sender, instance, **kwargs):
    subject = 'Registration deleted'
    message = f'A registration has been deleted with the following details:\n\nFull Name: {instance.full_name}\nPhone Number: {instance.phone_number}\nID Number: {instance.id_number}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL], fail_silently=True)
    logger.info(f"Registration delete email sent to {settings.ADMIN_EMAIL}")

post_save.connect(send_registration_delete_email, sender=Registration)    

