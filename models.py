from django.db import models
from django.conf import settings


class Order(models.Model):
 user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 item = models.CharField(max_length=200)
 created = models.DateTimeField(auto_now_add=True)