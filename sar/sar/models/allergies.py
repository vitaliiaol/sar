from django.db import models

class Allergies(models.Model):
    algname = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
    	db_table = 'allergies'