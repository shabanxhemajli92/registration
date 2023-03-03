from django import forms
from .models import Registration,Complaint,Appointment
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from io import BytesIO
from reportlab.pdfgen import canvas


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields=("full_name","phone_number","id_number")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)        

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'appointment_type', 'description']

    name = forms.CharField(max_length=100)
    appointment_type = forms.ChoiceField(choices=Complaint._meta.get_field('appointment_type').choices)
    description = forms.CharField(widget=forms.Textarea)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'date', 'time', 'location')


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
    
   
