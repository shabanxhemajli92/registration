from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('about/', AboutView.as_view(), name='about'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment'),
    path('appointment/success/', success_view, name='appointment_success'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('complaint/create/', ComplaintCreateView.as_view(), name='complaint'),
    path('complaint/list/', ComplaintListView.as_view(), name='complaint-list'),
    path('registration/list/', RegistrationListView.as_view(), name='registration_list'),
]