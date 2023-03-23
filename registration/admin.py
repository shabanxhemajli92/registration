from django.contrib import admin
from .models import Appointment,Registration,Complaint

admin.site.register(Appointment)
admin.site.register(Registration)
admin.site.register(Complaint)

#Username (leave blank to use 'dci-admin'): admin-real
#pass kosova1992