from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, ProductApplication, Industry, UserRequest


@admin.register(UserRequest)
class UserRequestAdmin(ModelAdmin):
    pass


@admin.register(Industry)
class IndustryAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductApplicationInline(TabularInline):
    model = ProductApplication
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductApplicationInline]
