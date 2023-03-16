from django.views.generic import ListView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from .forms import RegistrationForm,ContactForm,LoginForm,AppointmentForm
from django.views.generic import CreateView,ListView
from .models import Registration,Complaint
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from io import BytesIO
from reportlab.pdfgen import canvas




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
        appointment = form.save(commit=False)
        pdf_buffer = create_pdf(appointment)
        subject = 'Appointment Confirmation'
        message = 'Please find attached the details of your appointment.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = appointment.email

        email = EmailMessage(
            subject,
            message,
            from_email,
            [to_email],
            reply_to=[from_email],
        )
        email.content_subtype = 'html'
        email.attach('appointment.pdf', pdf_buffer.getvalue(), 'application/pdf')
        email.send()

        appointment.save()
        return super().form_valid(form)


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
        
class SuccessView(TemplateView):
    template_name = 'registration/appointment_success.html'