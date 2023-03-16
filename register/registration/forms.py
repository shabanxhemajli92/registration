from django import forms
from .models import Registration,Complaint,Appointment



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


        



