from django.urls import path,include
from . import views 

urlpatterns = [
    
   path('',views.index,name='ads'),
   #path('ad/',views.ad,name='ad')
   path('<int:ad_id>',views.ad,name='ad')
]
