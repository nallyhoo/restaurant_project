from django.db import models
import datetime
# Create your models here.

    
class Categories(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# class Drink(models.Model):
#     name = models.CharField(max_length=200)
#     price =models.DecimalField(default=0 ,decimal_places=2 , max_digits=10)
#     category = models.ForeignKey(Categories,on_delete=models.CASCADE , default=0)
#     image = models.ImageField(upload_to='uploads/product')
    
#     def __str__(self):
#         return self.name
    
    
# class Breakfast(models.Model):
#     name = models.CharField(max_length=200)
#     price =models.DecimalField(default=0 ,decimal_places=2 , max_digits=10)
#     category = models.ForeignKey(Categories,on_delete=models.CASCADE , default=0)
#     image = models.ImageField(upload_to='uploads/product')
    
#     def __str__(self):
#         return self.name
    
# class Lunch(models.Model):
#     name = models.CharField(max_length=200)
#     price =models.DecimalField(default=0 ,decimal_places=2 , max_digits=10)
#     category = models.ForeignKey(Categories,on_delete=models.CASCADE , default=0)
#     image = models.ImageField(upload_to='uploads/product')
    
#     def __str__(self):
#         return self.name
    
# class Dinner(models.Model):
#     name = models.CharField(max_length=200)
#     price =models.DecimalField(default=0 ,decimal_places=2 , max_digits=10)
#     category = models.ForeignKey(Categories,on_delete=models.CASCADE , default=0)
#     image = models.ImageField(upload_to='uploads/product')
    
#     def __str__(self):
#         return self.name
    
    
class Product(models.Model):    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250 ,default="" , blank=True , null=True )
    price =models.DecimalField(default=0 ,decimal_places=2 , max_digits=10)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE , default=0)
    image = models.ImageField(upload_to='uploads/product')
    
    def __str__(self):
        return self.name


    

    
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Sign_up(models.Model):
    email =models.CharField(max_length=100)
    username =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number =models.CharField(max_length=100) 


class Chef(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, default="", blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product', default="", blank=True, null=True)
    facebook_url = models.URLField(default="", blank=True, null=True)
    twitter_url = models.URLField(default="", blank=True, null=True)
    instagram_url = models.URLField(default="", blank=True, null=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    quantity_peo = models.CharField(max_length=20)
    special_req = models.TextField(max_length=200)
    is_approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    

class Online_order(models.Model):
    product_name =models.CharField(max_length=200)
    quantity_order =models.IntegerField()
    total_price = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=100)
    address_delivery =models.CharField(max_length=100)
    special_order= models.TextField(max_length=200)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name


