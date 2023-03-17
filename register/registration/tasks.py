from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Appointment

from .email import send_email_task

logger = get_task_logger(__name__)



@shared_task(name="send_email_task")
def email_task(appointment_pk):
    appointment = Appointment.objects.get(pk=appointment_pk)
    logger.info("Sending the email")
    send_email_task(appointment.name, appointment.email, appointment.date, appointment.time, appointment.location)
