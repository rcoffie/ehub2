from django.shortcuts import get_object_or_404, render,redirect 
from .models import *
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import *


# Create your views here.

def index(request):
  ads = Ads.objects.order_by('-date_posted').filter(published=True)
  paginator = Paginator(ads,6)
  page = request.GET.get('page')
  paged_ads = paginator.get_page(page)
  context = {'ads':paged_ads}
  return render(request,'ads/index.html',context)



def ad(request,ad_id):
  ad = get_object_or_404(Ads,pk=ad_id)
  context = {'ad':ad,}
  return render(request,'ads/ad.html',context)



def search(request):

  query_ads = Ads.objects.order_by('-date_posted')

  #keywords 
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      query_ads = query_ads.filter(description__icontains=keywords)

  
  #city 
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      query_ads = query_ads.filter(city__iexact=city)


  #Region
  if 'region' in request.GET:
    region = request.GET['region']
    if 'region':
      query_ads = query_ads.filter(region__iexact=region)

  
  #Category
  if 'category' in request.GET:
    category = request.GET['category']
    query_ads = query_ads.filter(category__iexact=category)

  context = {
    'ad_region': ad_region,
    'ad_category': ad_category,
    'ads':query_ads,
  }
  return render(request,'ads/search.html',context)