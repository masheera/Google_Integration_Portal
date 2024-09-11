from django.db import models
from accounts.models import Business
from django.conf import settings

class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
