from django.urls import path
from .views import HomeView, AboutView, RegistrationView, RegistrationListView,CustomLoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("login/",CustomLoginView.as_view(),name="login"),
    path('about/',AboutView.as_view(), name='about'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('registration-list/', RegistrationListView.as_view(), name='registration_list'),
]