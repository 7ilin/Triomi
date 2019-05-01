# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-30 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decor', '0005_auto_20190328_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='img')),
            ],
        ),
    ]
