from django.db import models

# Create your models here.
class Passenger(models.Model):
	firstname=models.CharField(max_length=10,primary_key=True)
	lastname=models.CharField(max_length=10)
	travelpoints=models.IntegerField()
