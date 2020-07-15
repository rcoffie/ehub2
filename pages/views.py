from django.shortcuts import render,redirect
from django.http import HttpResponse
from ads.choices import *
from ads.models import *

# Create your views here.


def index(request):
  ads = Ads.objects.order_by('-date_posted').filter(published=True)[:3]
  context= {
    'ads':ads,
    'ad_region':ad_region,
    'ad_category':ad_category,

  
  }
  return render(request,'pages/index.html',context)



def about(request):
  return render(request,'pages/about.html')




