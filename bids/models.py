from time import time
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Bid(models.Model):
    title = models.CharField(max_length=255)
    time = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    phone_number = models.PositiveIntegerField(max_length=10)
    adress = models.TextField()
    worker= models.TextField()           #models.ForeignKey(on_delete=models.CASCADE,)
    company = models.TextField()         #models.ForeignKey(on_delete=models.CASCADE,)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('bid_detail', args=[str(self.id)])