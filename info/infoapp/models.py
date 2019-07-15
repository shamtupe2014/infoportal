from django.db import models
from django.core.validators import MinLengthValidator

class register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField()
    team = models.CharField(max_length=20)


def __str__(self):
    return self.first_name


