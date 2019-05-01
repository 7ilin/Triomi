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
    name = models.CharField(max_length=250, verbose_name='Название')
    photo = models.ImageField(upload_to='img', blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.name


class Rent(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='img', blank=True, verbose_name='Фотография')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Стоимость')
    deposit = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Залог')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
