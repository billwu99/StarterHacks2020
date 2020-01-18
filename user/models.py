from datetime import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    current_weight = models.DecimalField(max_digits=10, decimal_places=2)
    desired_weight = models.DecimalField(max_digits=10, decimal_places=2)
    increment = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.email)
        