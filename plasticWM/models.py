from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class locality(models.Model):
    locality = models.CharField(max_length = 30)

    def __str__(self):
        return self.locality

class scrapshop(models.Model):
    locality = models.ForeignKey(locality , on_delete=models.DO_NOTHING)
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

    def __str__(self):
        return self.quality

class disposal(models.Model):
    userid = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    quality = models.IntegerField()
    shopid = models.ForeignKey(scrapshop , on_delete=models.DO_NOTHING)
    pickuprequired = models.BooleanField(default=False)
    disposaldone = models.BooleanField(default=False)
    disposaldate = models.DateField(default=timezone.now)

class pickup(models.Model):
    disposalid = models.IntegerField()
    agentid = models.IntegerField()
    pickupdate = models.DateField(default=timezone.now)
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
    locality = models.ForeignKey(locality , on_delete=models.DO_NOTHING)
    is_shopowner = models.BooleanField(default=False)
    is_pickperson = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE) 