from django.db import models
from django.db.models import ImageField,CharField,FloatField
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    product_image=ImageField(upload_to='images/')
    product_name=CharField(max_length=200)
    product_price=FloatField()
    stock = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.product_name

