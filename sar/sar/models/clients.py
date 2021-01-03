from django.db import models

class Clients(models.Model):
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.CharField(max_length=50)

    class Meta:
    	db_table = 'clients'