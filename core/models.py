from django.db import models


class ListModels(models.Model):
    ''' List models of cars '''
    idd = models.IntegerField(verbose_name="id")
    
class Cars(models.Model):
    'Description about car'
    idd = models.IntegerField(verbose_name="id")
    price = models.CharField(max_length=20, default="", verbose_name="price")
    title = models.CharField(max_length=20, default="", verbose_name="title")
    created = models.IntegerField(verbose_name="created")
    modified = models.IntegerField(verbose_name="modified")
    renewed = models.IntegerField(verbose_name="renewed")
    url = models.CharField(max_length=250, default="", verbose_name="url")

class OzonPoints(models.Model):
    name = models.CharField(max_length=250, verbose_name='name')
    address = models.CharField(max_length=250, verbose_name='address')
    deliveryType = models.CharField(max_length=250, verbose_name='deliveryType')
    metro = models.CharField(max_length=250, verbose_name='metro')