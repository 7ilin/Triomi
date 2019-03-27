from django.db import models
from django.utils import timezone


class Call(models.Model):

   #  https://hackernoon.com/using-enum-as-model-field-choice-in-django-92d8b97aaa63



    name = models.CharField(max_length=50, verbose_name='Имя')
    phone_number = models.CharField(max_length=12)
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()


    def __str__(self):
        return self.name
