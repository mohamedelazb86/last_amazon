from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.utils import timezone
from products.models import Product
from accounts.models import Address

ORDER_TYPE=[
    ('recieved','recieved'),
    ('processed','processed'),
    ('shipped','shipped'),
    ('delivered','delivered')
    ]
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='order_user')
    status=models.CharField(max_length=75,choices=ORDER_TYPE)
    code=models.CharField(max_length=75,default=generate_code)
    order_time=models.DateTimeField(default=timezone.now)
    delivery_time=models.DateTimeField(null=True,blank=True)
    delivery_address=models.ForeignKey(Address,related_name='order_address',on_delete=models.SET_NULL,null=True,blank=True)
    copoun=models.ForeignKey('Copoun',on_delete=models.SET_NULL,null=True,blank=True,related_name='order_copoun')
    total=models.FloatField(null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
    
class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='detail_order')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orderdetail_product')
    quantity=models.FloatField()
    price=models.FloatField()
    total=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.order)

CART_TYPE=[
    ('inprogress','inprogress'),
    ('completed','completed')

    ]  
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='cart_user')
    status=models.CharField(max_length=75,choices=CART_TYPE)
    copoun=models.ForeignKey('Copoun',on_delete=models.SET_NULL,null=True,blank=True,related_name='cart_copoun')
    total_with_copoun=models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
    
    @property
    def total_cart(self):
        total=0
        for item in self.detail_cart.all():
            total +=item.total
        return total
    
    
class Cart_Detai(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='detail_cart')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cartdetail_product')
    quantity=models.FloatField(default=1)
    
    total=models.FloatField(null=True,blank=True)

class Copoun(models.Model):
    code=models.CharField(max_length=120)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(null=True,blank=True)
    quantity=models.FloatField()
    discount=models.FloatField()

    def __str__(self):
        return str(self.code)
    
    def save(self,*args,**kwargs):
        week=timezone.timedelta(days=7)
        self.end_date = self.start_date +week
        super(Copoun,self).save(*args,**kwargs)

