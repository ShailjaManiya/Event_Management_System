from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    Name = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    Phone_No = models.IntegerField()
    Address = models.TextField()
    Gender = models.CharField(max_length=10)
    Dob = models.DateField()

    def __str__(self):
        return self.user.username
