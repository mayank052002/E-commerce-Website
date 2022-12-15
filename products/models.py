from django.db import models
class products(models.Model):
	category=models.CharField(max_length=30)
	product_id=models.CharField(max_length=100,default=0)
	brand_name=models.CharField(max_length=30)
	img_url=models.URLField(max_length=300)
	price=models.IntegerField()
	avl_quantity=models.IntegerField(default=0)
	specs=models.CharField(max_length=500)
	

   
