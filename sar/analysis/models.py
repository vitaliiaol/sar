from django.db import models


class Allergies(models.Model):
    algname = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'allergies'


class Components(models.Model):
    compname = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    firsthalf = models.IntegerField(max_length=1)
    secondhalf = models.IntegerField(max_length=1)
    allergies = models.ManyToManyField(Allergies)

    class Meta:
        db_table = 'components'
