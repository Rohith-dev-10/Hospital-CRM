from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    is_doctor = models.BooleanField(default=False)

# Create your models here.
