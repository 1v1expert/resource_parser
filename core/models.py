from django.db import models

class Cars(models.Model):
    'Description about car'
    idd = models.IntegerField(verbose_name="id")
    category = models.CharField(max_length=150, null=True, blank=True, default="", verbose_name="category")
    hasDamage = models.BooleanField(default=False, verbose_name='hasDamage')
    price = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="price")
    title = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="title")
    created = models.IntegerField(verbose_name="created")
    modified = models.IntegerField(verbose_name="modified")
    renewed = models.IntegerField(verbose_name="renewed")
    features = models.CharField(max_length=750, null=True, blank=True, default="", verbose_name="features")
    details = models.CharField(max_length=750, null=True, blank=True, default="", verbose_name="details")
    attr = models.CharField(max_length=750, null=True, blank=True, default="", verbose_name="attr")
    url = models.CharField(max_length=250, null=True, blank=True, default="", verbose_name="url")