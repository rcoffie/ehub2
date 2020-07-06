from django.shortcuts import render,redirect 
from .models import *
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def index(request):
  ads = Ads.objects.all()
  paginator = Paginator(ads,6)
  page = request.GET.get('page')
  paged_ads = paginator.get_page(page)
  context = {'ads':paged_ads}
  return render(request,'ads/index.html',context)