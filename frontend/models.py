from django.db import models

# Create your models here.
class regdb(models.Model):
    rname =models.CharField(max_length=100,null=True,blank=True)
    remail = models.CharField(max_length=100,null=True,blank=True)
    rmobile = models.IntegerField(max_length=100,null=True,blank=True)
    rpas = models.CharField(max_length=100,null=True,blank=True)
    rimage = models.ImageField(upload_to='user',null=True,blank=True)

class cartbd(models.Model):
    uname = models.CharField(max_length=100,null=True,blank=True)
    pname = models.CharField(max_length=100,null=True,blank=True)
    pdes = models.CharField(max_length=100,null=True,blank=True)
    pqu = models.CharField(max_length=100,null=True,blank=True)
    pprice = models.CharField(max_length=100,null=True,blank=True)
    ptotal = models.IntegerField(null=True,blank=True)
class billdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=100,null=True,blank=True)

