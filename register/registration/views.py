from django.views.generic import ListView,FormView,TemplateView,ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import Registration

class CustomLoginView(LoginView):
    template_name="registration/login.html"
    redirect_authenticated_user=True

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