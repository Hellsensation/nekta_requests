from django.contrib.auth.models import User
from django.db import models


class UserRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class RequestMessage(models.Model):
    text_message = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_request = models.ForeignKey(UserRequest, on_delete=models.PROTECT)

    def __str__(self):
        return self.text_message

