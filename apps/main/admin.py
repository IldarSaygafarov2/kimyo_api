from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, ProductApplication, Industry, UserRequest
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


@admin.register(UserRequest)
class UserRequestAdmin(ModelAdmin):
    list_display = ["id", "name", "phone_number", "company", "created_at"]
    sortable_by = ["created_at"]


@admin.register(Industry)
class IndustryAdmin(ModelAdmin, TranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductApplicationInline(TabularInline, TranslationTabularInline):
    model = ProductApplication
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductApplicationInline]
