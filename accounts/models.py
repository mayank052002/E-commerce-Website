from django.db import models
from django.contrib.auth.models import User
class Employee (models.Model):
	product_id=models.CharField(max_length=12)
	quantity=models.IntegerField()
	user=models.OneToOneField(User,on_delete=models.CASCADE)

