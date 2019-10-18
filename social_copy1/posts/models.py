from django.db import models
from groups.models import Group
# Create your models here.

import misaka

from django.contrib.auth.models import User


class Post(models.Model):
    user = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']