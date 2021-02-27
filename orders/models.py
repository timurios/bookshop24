from django.db import models
from products.models import *
from django.conf import settings 

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

def __str__(self):
    return self.user.username + "->" + self.product.name
# Create your models here.
