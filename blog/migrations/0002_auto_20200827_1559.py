# Generated by Django 3.1 on 2020-08-27 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Время написания'),
        ),
    ]
