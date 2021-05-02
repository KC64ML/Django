from django.db import models

# Create your models here.


class Sign_Up_Modle(models.Model):
    username = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=100)
    userage = models.CharField(max_length=100)
    useraddress = models.CharField(max_length=100)
    user_disability_rating = models.CharField(max_length=100)
