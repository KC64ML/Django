from django.db import models
# Create your models here.


class LoginModel(models.Model):
    useridx = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=45)
    userpassword = models.CharField(max_length=45)
