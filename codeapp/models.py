from django.db import models


# Create your models here.
class Point(models.Model):
    username=models.CharField(max_length=200)
    points=models.IntegerField()
    ques_attempted= models.IntegerField()

