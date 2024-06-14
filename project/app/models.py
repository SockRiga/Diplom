from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone


class Statment(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    set_time = models.DateTimeField(default=timezone.now(), verbose_name='Выбрать время', blank=False, null=False)
    image = models.ImageField(upload_to='post_images/', default='none')

    class Meta:
        ordering=["-created_at"]

class Service(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)
    image = models.ImageField(upload_to='service_images/', default=None, blank=True, null=True)

class Order(models.Model):
    contact = models.CharField(max_length=254, verbose_name="Почта или телефон", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)



