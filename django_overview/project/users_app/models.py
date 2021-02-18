from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255,unique=True)
    last_name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255,unique=True)