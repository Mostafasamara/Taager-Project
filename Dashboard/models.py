from django.db import models
# from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

# Create your models here.
class User(models.Model):
   username = models.CharField(max_length=200,blank=False)
   Addres = models.TextField(blank=False)
   phone_number = models.CharField(max_length=11,blank=False)

   def __str__(self):
       return self.username

class Category(models.Model):

    name = models.CharField(max_length=200,db_index=True)


    def __str__(self):
        return self.name
class Product(models.Model):
    uploaded = 'uploaded'
    INPROGRESS = 'in progress'

    CHOICES_STATUS = (
        (INPROGRESS, 'IN PROGRESS'),
        (uploaded, 'UPLOADED')

    )
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    real_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS)
    link = models.URLField(max_length=2000,blank=True)
    # code = models.

    def __str__(self):
        return self.name



class Orders(models.Model):
    DONE = 'done'
    INPROGRESS = 'in progress'

    CHOICES_STATUS = (
        (INPROGRESS, 'IN PROGRESS'),
        (DONE, 'Done')

    )
    user = models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='detalis',on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS)
