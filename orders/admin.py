from django.contrib import admin

from .models import Order,OrderDetail,Cart,Cart_Detai,Copoun

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(Cart_Detai)
admin.site.register(Copoun)
