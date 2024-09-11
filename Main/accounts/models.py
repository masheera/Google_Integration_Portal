from django.db import models
from django.conf import settings
# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
