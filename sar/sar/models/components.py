from django.db import models
from allergies.py import Allergies

class Components(models.Model):
    compname = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    firsthalf = models.IntegerField(max_length=1)
    secondhalf = models.IntegerField(max_length=1)
    secondhalf = models.ManyToManyFields(Allergies)

    class Meta:
    	db_table = 'components'