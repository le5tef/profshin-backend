from django.contrib import admin
from .models import Property, Product, ProductProperty, Category
from .forms import PropertyForm


@admin.register(ProductProperty, Property, Category)
class AuthorAdmin(admin.ModelAdmin):
    pass


class ProductPropertyInline(admin.TabularInline):
    model = ProductProperty
    form = PropertyForm
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductPropertyInline,
    ]
