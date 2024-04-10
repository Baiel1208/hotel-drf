from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    position = models.CharField(max_length=100)