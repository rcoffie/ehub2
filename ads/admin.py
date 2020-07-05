from django.contrib import admin
from .models import *


class AdsAdmin(admin.ModelAdmin):
  list_display = ('id','title','seller','city','region','price','published','negotiable','date_posted','published','used')
  list_display_links = ('title','seller')
  list_filter = ('title','seller','price','city','region',)
  list_editable = ('id','negotiable','published','used')
  search_fields = ('title','seller','price','city','region')
  list_per_page  = 12


# Register your models here.
admin.site.register(Ads,AdsAdmin)