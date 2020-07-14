from django.db import models
from sellers.models import Seller
from datetime import datetime 
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Ads(models.Model):
  Category=(
    ('Mobile Phones','Mobile Phones'),
    ('Mobile Phone Accessories','Mobile Phone Accessories'),
    ('Computer Accessories','Computer Accessories'),
    ('TVs','TVs'),
     ('TV & Video Accessories','TV & Video Accessories'),
    ('Cameras & Camcorders','Cameras & Camcorders'),
    ('Audio & MP3','Audio & MP3'),
    ('Other Electronics','Other Electronics'),
   )

  Region=(
    ('Upper West','Upper West'),
    ('Upper East','Upper East'),
    ('North East','North East'),
    ('Northen','Northen'),
     ('Savannah','Savannah'),
    ('Bono East','Bono East'),
    ('Brong Ahafo','Brong Ahafo'),
    ('Oti','Oti'),
    ('Ahafo','Ahafo'),
    ('Ashanti','Ashanti'),
    ('Volta','Volta'),
    ('Greater Accra','Greater Accra'),
    ('Western North','Western North'),
    ('Western','Western'),
    ('Eastern','Eastern'),
    ('Central','Central'),
   )
  
  
  title = models.CharField(max_length=100)
  seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
  category = models.CharField(max_length=200, null=True,choices=Category)
  city = models.CharField(max_length=50)
  region = models.CharField(max_length=200, null=True,choices=Region)
  description = models.TextField()
  price  = models.IntegerField()
  brand  = models.CharField(max_length=200,null=True)
  phone_number = PhoneNumberField(null=True)
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