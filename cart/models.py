from django.db import models
class product_entry(models.Model):
	product_id=models.CharField(max_length=12)
	quantity=models.IntegerField()
	user=models.CharField(max_length=30)
	price=models.IntegerField(default=0)
	img_url=models.URLField(max_length=301)
	brand_name=models.CharField(max_length=30)
	category=models.CharField(max_length=30)
	subtotal=models.IntegerField(default=0)
	
