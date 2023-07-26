from django.db import models

# Create your models here.
class catdb(models.Model):
    cname = models.CharField(max_length=100,null=True,blank=True)
    cdes = models.CharField(max_length=200,null=True,blank=True)
    cimage = models.ImageField(upload_to='category',null=True,blank=True)

class productdb(models.Model):
    pselect = models.CharField(max_length=100,null=True,blank=True)
    pname = models.CharField(max_length=100,null=True,blank=True)
    pdes = models.CharField(max_length=100,null=True,blank=True)
    pprice = models.CharField(max_length=100,null=True,blank=True)
    pimage = models.ImageField(upload_to='vechicles',null=True,blank=True)
