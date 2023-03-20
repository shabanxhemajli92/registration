from django.urls import path, include
from rest_framework import routers
from .views import RegistrationViewSet, ComplaintViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'registrations', RegistrationViewSet)
router.register(r'complaints', ComplaintViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('/v1/', include(router.urls)),
]