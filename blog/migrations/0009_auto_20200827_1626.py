# Generated by Django 3.1 on 2020-08-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200827_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(auto_now=True, verbose_name='Время написания'),
        ),
    ]
