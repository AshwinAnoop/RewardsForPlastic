from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class locality(models.Model):
    locality = models.CharField(max_length = 30)

class scrapshop(models.Model):
    locality = models.CharField(max_length = 30)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    capacity = models.IntegerField()
    stockloaded = models.IntegerField()
    image = models.ImageField(upload_to = 'pics/')
    gmaplink = models.CharField(max_length = 150)
    shopmobile = models.CharField(max_length = 12)

class wasteprice(models.Model):
    quality = models.CharField(max_length = 30)
    priceperkg = models.IntegerField()

class disposal(models.Model):
    userid = models.IntegerField()
    quantity = models.IntegerField()
    quality = models.IntegerField()
    shopid = models.IntegerField()
    pickuprequired = models.BooleanField(default=False)

class pickup(models.Model):
    disposalid = models.IntegerField()
    agentid = models.IntegerField()
    pickupdate = models.DateField()
    confirmation = models.BooleanField(default=False)
    charges = models.IntegerField()

class rewards(models.Model):
    userid = models.IntegerField()
    rewards = models.IntegerField()

class shoppayment(models.Model):
    shopid = models.IntegerField()
    collectedqty = models.IntegerField()
    payment = models.IntegerField()
    daterecieved = models.DateField()


class extendeduser(models.Model):
    mobile = models.CharField(max_length = 12)
    address = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE) 