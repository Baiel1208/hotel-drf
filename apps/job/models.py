from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    earnings = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/')
