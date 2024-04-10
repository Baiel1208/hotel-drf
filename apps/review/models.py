from django.db import models

# Create your models here.
class Review(models.Model):
    video_link = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='review_images/')