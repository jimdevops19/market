from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchased_items', null=True, blank=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    