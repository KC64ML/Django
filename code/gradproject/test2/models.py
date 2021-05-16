from django.db import models

# Create your models here.


class LoginModels(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'test2_loginmodels'
