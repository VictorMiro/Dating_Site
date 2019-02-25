from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from messagesOF.managers import PostManager


class Messages(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='outbox', on_delete=models.CASCADE, null=True)
    text_of = models.TextField()
    date_of = models.DateTimeField(auto_now=True)
    reciver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='inbox', on_delete=models.CASCADE, null=True)
    order_manager = PostManager()

    def __str__(self):
        return f'Dialog {self.user}'
