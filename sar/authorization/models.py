from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'clients'

