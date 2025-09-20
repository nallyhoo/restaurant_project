from django.contrib import admin
from myapp.models import Categories , Product , Contact,Sign_up, Chef ,Booking ,Online_order
# Register your models here.

admin.site.site_header='Cafe | Restuarant Admin'

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category']
    
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','is_approved']
    
class AccountAdmin(admin.ModelAdmin):
    list_display=['username','password']
    
class list_chef(admin.ModelAdmin):
    list_display=['id','name','designation']
    
class list_booking(admin.ModelAdmin):
    list_display=['id','name','date','quantity_peo','is_approved']
    
class list_order(admin.ModelAdmin):
    list_display=['id','fullname','quantity_order','total_price','is_approved']

admin.site.register(Categories)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Sign_up,AccountAdmin)
admin.site.register(Chef,list_chef)
admin.site.register(Booking,list_booking)
admin.site.register(Online_order,list_order)
