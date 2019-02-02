from django.db import models
from django.contrib.auth.models import User


class AgeOfUSER(models.Model):
    age = models.IntegerField(default=20)

    class Meta:
        verbose_name = 'Возраст пользователя'
        verbose_name_plural = 'Возроста пользователей'


class RatingOFUSER(models.Model):
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Рейтинг пользователя'
        verbose_name_plural = 'Рейтинг пользователей'


class CategoryOFUSER(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория пользователя'
        verbose_name_plural = 'Категории пользователей'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image_of_user')
    age = models.ForeignKey(AgeOfUSER, on_delete=models.CASCADE)
    rating = models.ForeignKey(RatingOFUSER, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryOFUSER, on_delete=models.CASCADE)
    registration_at = models.DateTimeField(auto_now=True)
    bio = models.TextField()

    class Meta:
        ordering = ["rating"]
