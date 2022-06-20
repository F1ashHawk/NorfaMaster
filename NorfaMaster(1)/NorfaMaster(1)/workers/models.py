from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Worker(models.Model):
    title = models.CharField(max_length=255)
    schedule = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    rating = models.PositiveIntegerField(max_length=1)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('worker_detail', args=[str(self.id)])