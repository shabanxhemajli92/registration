from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RegistrationSerializer, ComplaintSerializer, AppointmentSerializer
from registration.models import Registration, Complaint, Appointment

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer