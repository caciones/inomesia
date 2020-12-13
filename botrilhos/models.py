from django.db import models


# Create your models here.



class Route(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    distance = models.FloatField(default='')
    loop = models.BooleanField(default=False)
    published = models.BooleanField(default=False)


class Local(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, blank = True, null = True)