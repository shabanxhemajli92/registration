from django import forms
from .models import Registration

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
        