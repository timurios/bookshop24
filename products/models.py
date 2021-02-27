from django.db import models
from django.conf import settings
from django.utils import timezone


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    genre = models.TextField(default="")
    writer = models.TextField(default="")
    image = models.TextField(default="")

    created_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.name
# Create your models here.
