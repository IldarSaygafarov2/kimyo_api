from django.contrib import admin

from .models import Category, Product, ProductApplication, Industry, UserRequest
# from constance.admin import Config, ConstanceAdmin


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductApplicationInline(admin.TabularInline):
    model = ProductApplication
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductApplicationInline]
