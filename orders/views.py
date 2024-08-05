from django.shortcuts import render,redirect
from .models import Order,Cart_Detai,Cart,Copoun
from settings.models import Delivery_Fee
from django.shortcuts import get_object_or_404
import datetime
from products.models import Product

def order_list(request):
    orders=Order.objects.filter(user=request.user)

    context={
        'orders':orders
    }
    return render(request,'orders/order_list.html',context)

def checkout(request):

    cart=Cart.objects.get(user=request.user,status='inprogress')
    cart_detail=Cart_Detai.objects.filter(cart=cart)
    
    delivery_fee=Delivery_Fee.objects.last().fee
    

    if request.method=='POST':
        #copoun=Copoun.objects.get(code=request.POST['copoun_code'])
        copoun=get_object_or_404(Copoun,code=request.POST['copoun_code'])
        if copoun and copoun.quantity > 0:
            mytody=datetime.datetime.today().date()
            if mytody >= copoun.start_date and mytody <= copoun.end_date:
                copoun_value=cart.total_cart /100*copoun.discount
                subtotal=cart.total_cart 

                total=subtotal+delivery_fee-copoun_value

                cart.total_with_copoun=subtotal

                copoun.quantity -=1
                copoun.save()

                cart.save()

                context={
                    'cart':cart,
                    'cart_detail':cart_detail,
                    'subtotal':subtotal,
                    'delivery_fee':delivery_fee,
                    'discount':copoun_value,
                    'total':total

                                    
                       }

                return render(request,'orders/checkout.html',context)

                



    subtotal=cart.total_cart
    total=subtotal+delivery_fee
    context={
        'cart':cart,
        'cart_detail':cart_detail,
        'subtotal':subtotal,
        'delivery_fee':delivery_fee,
        'discount':0,
        'total':total
    }

 
    return render(request,'orders/checkout.html',context)


def add_cart(request):

    product=Product.objects.get(id=request.POST['product_id'])
    quantity=int(request.POST['quantity'])

    cart=Cart.objects.get(user=request.user,status='inprogress')
    cart_detail,created=Cart_Detai.objects.get_or_create(cart=cart,product=product)

    cart_detail.quantity=quantity
    cart_detail.total=round(cart_detail.quantity*product.price)

    cart_detail.save()

    return redirect(f'/products/{product.slug}')

   

