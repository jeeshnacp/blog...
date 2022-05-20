from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user=models.BooleanField(default=False)

class user(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    contact_no=models.IntegerField()
    email=models.EmailField()
