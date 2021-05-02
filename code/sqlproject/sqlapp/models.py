from django.db import models


class Login(models.Model):
    usernumber = models.AutoField(primary_key=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    username_id_field = models.CharField(
        db_column='username(id)', max_length=45)
    userpassword = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'login'


class SignUp(models.Model):
    usernumber = models.AutoField(primary_key=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    username_id_field = models.CharField(
        db_column='username(id)', max_length=45)
    userpassword = models.CharField(max_length=45)
    userage = models.CharField(max_length=45, blank=True, null=True)
    useraddress = models.CharField(max_length=45, blank=True, null=True)
    user_disability_rating = models.CharField(
        max_length=45, blank=True, null=True)
    login_usernumber = models.ForeignKey(
        Login, models.DO_NOTHING, db_column='login_usernumber')

    class Meta:
        managed = False
        db_table = 'sign_up'
        unique_together = (('usernumber', 'login_usernumber'),)
