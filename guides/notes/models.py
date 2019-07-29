from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='default subtitle')
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'id: {self.id}, title: {self.title}'


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
