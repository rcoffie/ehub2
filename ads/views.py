from django.shortcuts import render,redirect 
from .models import *

# Create your views here.

def index(request):
  ads = Ads.objects.all()
  context = {'ads':ads}
  return render(request,'ads/index.html',context)