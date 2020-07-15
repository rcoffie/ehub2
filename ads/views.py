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
  
  context = {
    'ad_region': ad_region,
    'ad_category': ad_category,
  }
  return render(request,'ads/search.html',context)