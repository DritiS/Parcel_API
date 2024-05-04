from django.db import models

# Create your models here.
class Parcel(models.Model):
    name = models.CharField(max_length=100)
    parcel_id = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=10)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.parcel_id
