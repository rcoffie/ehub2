from django.db import models
from sellers.models import Seller
from datetime import datetime 

# Create your models here.

class Ads(models.Model):
  title = models.CharField(max_length=100)
  seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
  city = models.CharField(max_length=50)
  region = models.CharField(max_length=50)
  description = models.TextField()
  price  = models.IntegerField()
  published = models.BooleanField(default=False)
  negotiable = models.BooleanField(default=False)
  used = models.BooleanField(default=False)
  main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
  date_posted = models.DateField(default=datetime.now, blank=True)


  def __str__(self):
    return self.title 