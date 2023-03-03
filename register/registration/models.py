from django.db import models

class Registration(models.Model):
    full_name=models.CharField(max_length=100)
    phone_number=models.IntegerField(max_length=30)
    id_number=models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    appointment_type = models.CharField(
        max_length=20,
        choices=[
            ('passport', 'Passport'),
            ('id', 'ID'),
            ('driverslicence', "Driver's Licence"),
            ('utilitybill', 'Utility Bill'),
        ],
    ) 
    description = models.TextField(default='No description provided') 
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} {self.appointment_type}"

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name