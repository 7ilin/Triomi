from django.db import models
from django.utils import timezone


class Call(models.Model):

    WAITING = '0'
    DURING = '1'
    FULFILLED = '2'
    STATUS_CHOICES = (
        (WAITING, 'Ожидает'),
        (DURING, 'В процессе'),
        (FULFILLED, 'Выполнен'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=WAITING,
    )

    name = models.CharField(max_length=50, verbose_name='Имя')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=250, verbose_name='Описание')
    photo = models.ImageField(upload_to='img', blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.name
