from django.db import models
from django.contrib.auth.models import User


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


class Profile(models.Model):
    TYPE_MALE = 0
    TYPE_FEMALE = 1
    TYPE_NOT_SELECTED = 2

    TYPE_CHOICES = (
        (TYPE_MALE, 'MALE'),
        (TYPE_FEMALE, 'FEMALE'),
        (TYPE_NOT_SELECTED, 'NOT_SELECTED')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    rating = models.PositiveIntegerField()
    category = models.ForeignKey(CategoryOFUSER, on_delete=models.CASCADE)
    registration_at = models.DateTimeField(auto_now=True)
    gender = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_NOT_SELECTED)
    city = models.ForeignKey(CityOFUSER, on_delete=models.SET_NULL, null=True)
    bio = models.TextField()

    class Meta:
        ordering = ["rating"]

    def __str__(self):
        return self.name
