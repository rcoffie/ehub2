from django.contrib import admin
from .models import *


class SellerAdmin(admin.ModelAdmin):
  list_display = ('id','name','phone','email','join_date')
  list_display_links = ('id','name')
  list_filter = ('name',)
  search_fields = ['name',]
  list_per_page = 10

# Register your models here.
admin.site.register(Seller,SellerAdmin)