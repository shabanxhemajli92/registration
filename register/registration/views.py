from django.views.generic import ListView,FormView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import Registration

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