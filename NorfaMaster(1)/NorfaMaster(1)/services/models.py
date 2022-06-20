from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    schedule = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    cost = models.PositiveIntegerField(max_length=7)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])