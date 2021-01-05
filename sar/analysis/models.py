from django.db import models


class Allergies(models.Model):
    algname = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'allergies'


class Components(models.Model):
    compname = models.CharField(max_length=50, primary_key=False)
    description = models.CharField(max_length=1000)
    firsthalf = models.IntegerField()
    secondhalf = models.IntegerField()
    allergies = models.ManyToManyField(Allergies)

    class Meta:
        db_table = 'components'


class Analysis(models.Model):
    verdict = models.CharField(max_length=50)
    percentage = models.FloatField()
    influences = models.CharField(max_length=500)

    class Meta:
        db_table = 'analysis'
