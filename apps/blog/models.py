from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images/')
    views = models.PositiveIntegerField(default=0)