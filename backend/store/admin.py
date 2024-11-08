# admin.py

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Product, Color, Size, Specification, Gallery

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'category', 'shipping_amount', 'stock_qty', 'in_stock', 'vendor', 'featured')

class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 0

class SpecificationInLine(admin.TabularInline):
    model = Specification
    extra = 0

class ColorInLine(admin.TabularInline):
    model = Color
    extra = 0

class SizeInLine(admin.TabularInline):
    model = Size
    extra = 0

@admin.register(Product)
class ProductsAdmin(ImportExportModelAdmin):
    resource_class = ProductResource  # Enable import/export for Product model
    list_display = ["title", "price", "category", "shipping_amount", "stock_qty", "in_stock", "vendor", "featured"]
    # list_editable = ["featured"]
    search_fields = ["title"]
    list_filter = ["date"]
    inlines = [GalleryInLine, SpecificationInLine, ColorInLine, SizeInLine]

# Optionally, register admin classes for other models if bulk upload for them directly is needed

