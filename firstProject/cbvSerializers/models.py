from django.db import models

# Create your models here.
class Course(models.Model):
	name=models.CharField(max_length=10,primary_key=True)
	description=models.CharField(max_length=25)
	ratings=models.IntegerField()
