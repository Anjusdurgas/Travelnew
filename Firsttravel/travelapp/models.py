from django.db import models
from pip._internal.utils._jaraco_text import _


# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')#pics is a folder name means where to upload the img
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')  # pics is a folder name means where to upload the img
    desc = models.TextField()

    def __str__(self):
        return self.name  #to view the name that we given in the admin panel for a parti. image

class User(models.Model):
    username = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email=models.CharField(max_length=100)
    password=models.CharField(_('password'), max_length=128)


    def __str__(self):
        return self.name  #to view the name that we given in the admin panel for a parti. image