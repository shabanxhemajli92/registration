from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def create_pdf(appointment):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, "Appointment Confirmation")
    pdf.drawString(100, 700, f"Name: {appointment.name}")
    pdf.drawString(100, 650, f"Date: {appointment.date}")
    pdf.drawString(100, 600, f"Time: {appointment.time}")
    pdf.drawString(100, 550, f"Location: {appointment.location}")
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')