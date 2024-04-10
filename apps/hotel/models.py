from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotel_images/')