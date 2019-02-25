from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='all_images')
    object_id = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    obj = GenericForeignKey


class CategoryOFUSER(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория пользователя'
        verbose_name_plural = 'Категории пользователей'


class CityOFUSER(models.Model):
    name = models.CharField(max_length=255)
    places = models.TextField()

    class Meta:
        verbose_name = 'Город пользователя'
        verbose_name_plural = 'Города пользователей'


class CustomUser(AbstractUser):

    TYPE_MALE = 0
    TYPE_FEMALE = 1
    TYPE_NOT_SELECTED = 2

    TYPE_CHOICES = (
        (TYPE_MALE, 'MALE'),
        (TYPE_FEMALE, 'FEMALE'),
        (TYPE_NOT_SELECTED, 'NOT_SELECTED')
    )
    avatar = models.ImageField(blank=True, null=True, upload_to='user_avatars')
    age = models.IntegerField(blank=True, null=True,)
    rating = models.PositiveIntegerField(blank=True, null=True,)
    category = models.ForeignKey(CategoryOFUSER, on_delete=models.CASCADE, blank=True, null=True,)
    gender = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_NOT_SELECTED)
    city = models.ForeignKey(CityOFUSER, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True, null=True,)
    phone = models.CharField(max_length=255, blank=True, null=True)
