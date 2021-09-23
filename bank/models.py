from django.db import models
from django.conf import settings
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
