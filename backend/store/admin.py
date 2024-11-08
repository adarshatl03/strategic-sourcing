from django.contrib import admin
from .models import Product,Color,Size,Specification,Gallery
# Register your models here.
class GalleryInLine(admin.TabularInline):
    model=Gallery 
    extra=0

class SpecificationInLine(admin.TabularInline):
    model=Specification 
    extra=0
class ColorInLine(admin.TabularInline):
    model=Color 
    extra=0
class SizeInLine(admin.TabularInline):
    model=Size 
    extra=0
class ProductsAdmin(admin.ModelAdmin):
    list_display=["title","price","category","shipping_amount","stock_qty","in_stock","vendor","featured"]
    list_editable=["featured"]
    search_fields=["title"]
    list_filter=["date"]
    inlines=[GalleryInLine,SpecificationInLine,ColorInLine,SizeInLine]

admin.site.register(Product,ProductsAdmin)
