# Generated by Django 3.1 on 2020-08-27 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200827_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 16, 0, 54, 811697), verbose_name='Время написания'),
        ),
    ]
