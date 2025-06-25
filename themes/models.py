from django.db import models

# Create your models here.
class Sitesettings(models.Model):
    banner=models.ImageField(upload_to='media/python')
