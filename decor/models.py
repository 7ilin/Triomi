from django.db import models
from django.utils import timezone


class Call(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
