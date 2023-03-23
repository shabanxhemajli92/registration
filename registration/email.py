from django.core.mail import EmailMessage
from io import BytesIO
from django.conf import settings
from reportlab.pdfgen import canvas
from .models import Appointment


def send_email_task(name, email, date, time, location):
    appointment = Appointment(name=name, email=email, date=date, time=time, location=location)
    pdf_buffer = create_pdf(appointment)
    subject = 'Appointment Confirmation'
    message = 'Please find attached the details of your appointment.'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = email

    email = EmailMessage(
        subject,
        message,
        from_email,
        [to_email],
        reply_to=[from_email],
    )
    email.content_subtype = 'html'
    email.attach('appointment.pdf', pdf_buffer.getvalue(), 'application/pdf')
    return email.send()
def create_pdf(appointment):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Appointment Confirmation for {appointment.name}")
    p.drawString(100, 700, f"Date: {appointment.date}")
    p.drawString(100, 650, f"Time: {appointment.time}")
    p.drawString(100, 600, f"Location: {appointment.location}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer