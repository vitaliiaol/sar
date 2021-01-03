from django.db import models
from clients.py import Clients

class Users(models.Model):
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=72)
    usertype = models.CharField(max_length=5)
    clientid = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
    	db_table = 'users'