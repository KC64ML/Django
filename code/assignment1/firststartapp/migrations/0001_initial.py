# Generated by Django 3.2 on 2021-05-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('useridx', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=45)),
                ('userpassword', models.CharField(max_length=45)),
            ],
        ),
    ]
