from .models import Cart,Cart_Detai

def get_context_data(request):
    if request.user.is_authenticated:
        cart,created=Cart.objects.get_or_create(user=request.user,status='inprogress')
        cart_detail=Cart_Detai.objects.filter(cart=cart)

        return {'cart':cart,'cart_detail':cart_detail}
    else:
        return {}
