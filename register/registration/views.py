from django.views.generic import ListView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from .forms import RegistrationForm,ContactForm,LoginForm,AppointmentForm
from django.views.generic import CreateView,ListView
from .models import Registration,Complaint,Appointment
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render
from .utils import create_pdf





class LoginView(FormView):
    form_class=LoginForm
    template_name="registration/login.html"
    success_url=reverse_lazy("home")

    

class HomeView(TemplateView):
    template_name = 'registration/home.html'

class AboutView(TemplateView):
    template_name = 'registration/about.html'

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('registration_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class RegistrationListView(ListView):
    model = Registration
    template_name = 'registration/registered.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'registration/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        subject = f'New contact message from {name}'
        body = f'{name} sent a message:\n\n{message}'
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

        return super().form_valid(form)


class MyLogoutView(TemplateView):
    template_name = 'registration/logut.html'
    success_url = reverse_lazy('login')        


class ComplaintCreateView(CreateView):
    model = Complaint
    fields = ['name', 'appointment_type','description']
    success_url = reverse_lazy('complaint-list')
    template_name = 'registration/complaint_form.html'

class ComplaintListView(ListView):
    model = Complaint
    template_name = 'registration/complaint_list.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['name', 'email', 'date', 'time', 'location']
    template_name = 'registration/appointment_form.html'
    success_url = reverse_lazy('appointment_success')

    def send_email(self):
        appointment = self.object
        pdf = create_pdf(appointment)
        subject = 'Appointment Confirmation'
        message = render_to_string('registration/appointment_email.html', {'appointment': appointment})
        email = EmailMessage(subject, message, to=[appointment.email])
        email.content_subtype = 'html' 
        email.attach(f'{appointment.name}.pdf', pdf.getvalue(), 'application/pdf')
        email.send()

    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_email()
        return response

def success_view(request):
    return render(request, 'registration/appointment_success.html')