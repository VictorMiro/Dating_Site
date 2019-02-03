from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_of = models.TextField()
    date_of = models.DateTimeField(auto_now=True)
    reciver = models.ForeignKey(User, on_delete=models.CASCADE)
