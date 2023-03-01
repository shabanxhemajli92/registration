from django.db import models

class Registration(models.Model):
    full_name=models.CharField(max_length=100)
    phone_number=models.IntegerField(max_length=30)
    id_number=models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

