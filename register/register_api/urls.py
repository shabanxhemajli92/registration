from django.urls import path, include
from rest_framework import routers
from .views import RegistrationViewSet, ComplaintViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register('registrations', RegistrationViewSet)
router.register('complaints', ComplaintViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]