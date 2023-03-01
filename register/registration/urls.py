from django.urls import path
from .views import RegistrationView, RegistrationListView

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('list/', RegistrationListView.as_view(), name='registration_list'),
]