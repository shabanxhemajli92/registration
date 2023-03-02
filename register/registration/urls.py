from django.urls import path
from .views import HomeView, AboutView, RegistrationView, RegistrationListView,LoginView,ContactView,MyLogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("login/",LoginView.as_view(),name="login"),
    path('logut/',MyLogoutView.as_view(),name='logout'),
    path('about/',AboutView.as_view(), name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('registration-list/', RegistrationListView.as_view(), name='registration_list'),
]