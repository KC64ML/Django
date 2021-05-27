from django.db import models
# Create your models here.


class LoginModel(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()

    class meta:
        ordering = {'created'}
