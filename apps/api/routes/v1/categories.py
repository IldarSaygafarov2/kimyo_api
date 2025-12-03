from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ninja import Router

from apps.api.schemas.category import CategorySchema, CategoryProductSchema
from apps.main.models import Category


router = Router(
    tags=["Категории"],
)


@router.get("/", response=list[CategorySchema])
def get_categories(request: HttpRequest):
    categories = Category.objects.all()
    return categories


@router.get('/{slug}', response=CategoryProductSchema)
def get_category_by_slug(request: HttpRequest, slug: str):
    category = get_object_or_404(Category, slug=slug)
    return category
