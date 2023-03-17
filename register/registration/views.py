from django.views.generic import ListView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from .forms import RegistrationForm,ContactForm,LoginForm,AppointmentForm
from django.views.generic import CreateView,ListView
from .models import Registration,Complaint
from django.conf import settings
from django.core.mail import send_mail
from .tasks import email_task








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

class AppointmentFormView(FormView):
    form_class = AppointmentForm
    template_name = 'registration/appointment_form.html'
    success_url = reverse_lazy('appointment_success')

    def form_valid(self, form):
        appointment = form.save(commit=True)
        appointment.save()
        email_task.apply_async(args=[appointment.pk], countdown=4)
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'registration/appointment_success.html'