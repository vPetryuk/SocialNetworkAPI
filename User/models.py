from django.db import models

class photos(models.Model):
    smallphoto =models.CharField(max_length=1000)
    bigphoto =models.CharField(max_length=1000)

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=50)
    status = models.CharField(max_length=50,blank=True)
    photos = models.OneToOneField(photos, on_delete=models.CASCADE,blank=True)

