from django.contrib import admin

# Register your models here.
from cart import models
class product_entryAdmin(admin.ModelAdmin):
	list_display=['product_id','user','quantity','img_url','category','brand_name','price','subtotal']
admin.site.register(models.product_entry,product_entryAdmin)