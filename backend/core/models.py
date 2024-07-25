from django.db import models
from django.contrib.auth.models import User

# pass - havish@123 - harsh
#        rojha123  - rohit
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True) # one user can add many products so Product is in ManyToOne replationship with user
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)  
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    name = models.CharField(max_length=30, blank=True, null= True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.rating)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    paymentMethod = models.CharField(max_length=30, blank=True, null= True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliverdAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    name = models.CharField(max_length=200, blank=True, null= True)
    qty = models.IntegerField(null=True, blank=True, default= 0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, blank=True, null= True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name
    
    
class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True) # one to one relationship
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=200, blank=True, null= True)
    postalCode = models.CharField(max_length=200, blank=True, null= True)
    country = models.CharField(max_length=200, blank=True, null= True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)