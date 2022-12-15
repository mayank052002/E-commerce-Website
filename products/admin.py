from django.contrib import admin
from products import models
class productsAdmin(admin.ModelAdmin):
	list_display=['category','product_id','brand_name','img_url','price','avl_quantity','specs']
admin.site.register(models.products,productsAdmin)