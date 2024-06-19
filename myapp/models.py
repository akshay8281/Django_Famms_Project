from django.db import models
from django.utils import timezone

# Create your models here.

# User
class User(models.Model):
	fname = models.CharField(max_length = 100)
	lname = models.CharField(max_length = 100)
	email = models.EmailField()
	mobile = models.PositiveIntegerField()
	address = models.TextField()
	password = models.CharField(max_length = 100)
	usertype = models.CharField(max_length = 100,default = "Buyer")
	profile_picture = models.ImageField(upload_to = "profile_picture/",default = "")
	
	def __str__(self) :
		return self.fname + " " + self.lname


# Product
class Product(models.Model):
	category = (
		("Men","Men"),
		("Women","Women"),
		("Kids","Kids"),
	)
	sub_category = (
		("Jeans","Jeans"),
		("T-Shirt","T-Shirt"),
		("Shirts","Shirts"),
	)

	seller = models.ForeignKey(User,on_delete = models.CASCADE)
	product_category = models.CharField(max_length=100,choices = category)
	product_sub_category = models.CharField(max_length=100,choices = sub_category)
	product_name = models.CharField(max_length=100)
	product_price = models.PositiveIntegerField()
	product_image = models.ImageField(upload_to = "product_image/")
	product_desc = models.TextField()

	def __str__(self):
		return self.seller.fname + " - " + self.product_name

# Wishlist

class Wishlist(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.user.fname + " - " + self.product.product_name


# Cart

class Cart(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	date = models.DateTimeField(default = timezone.now)
	product_price = models.PositiveIntegerField()
	product_qty = models.PositiveIntegerField()
	total_price = models.PositiveIntegerField()
	payment_status = models.BooleanField(default = False)

	def __str__(self):
		return self.user.fname + " - " + self.product.product_name