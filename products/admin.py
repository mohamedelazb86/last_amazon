from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Brand,ProductImage,Review

class Product_imageAdmin(admin.TabularInline):
    model=ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','price','flag','sku']
    search_fields=['name','subtitle','descriptions']
    list_filter=['brand']

    summernote_fields = ('subtitle','descriptions')
    inlines=[Product_imageAdmin]

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
#admin.site.register(ProductImage)
admin.site.register(Review)
