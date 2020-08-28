from datetime import datetime

from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

#User = get_user_model()

class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок публикации", max_length=1024)
    content = models.TextField(verbose_name="Содержание публикации", blank=False)
    #published_date = models.DateField(default = datetime.now(), verbose_name="Время написания")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Время написания",)
    image = models.ImageField(verbose_name="Картинка")
    #slug = models.SlugField(unique=True)

    #def get_absolute_url(self):
    #    return reverse('blog:post', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'