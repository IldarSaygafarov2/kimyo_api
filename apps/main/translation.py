from modeltranslation.translator import translator, TranslationOptions

from .models import Industry, Category, Product, ProductApplication

# name
# description_1
# description_2


class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description_1", "description_2")


class ProductApplicationTranslationOptions(TranslationOptions):
    fields = ("name", "description")


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", "short_description")


class IndustryTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Industry, IndustryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductApplication, ProductApplicationTranslationOptions)
