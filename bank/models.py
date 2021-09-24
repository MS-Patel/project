from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey


# Create your models here.


class Landing(models.Model):
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, unique=False)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=150)
    balance = models.FloatField(default=0)
    credit = models.FloatField(default=0)
    debit = models.FloatField(default=0)

    def __str__(self):
        return self.full_name


class UserOtp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()
