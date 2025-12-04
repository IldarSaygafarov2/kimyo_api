from ninja import Router
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from apps.api.schemas.product import ProductDetailSchema, ProductSimpleSchema
from apps.main.models import Product


router = Router(
    tags=["Товары"],
)


@router.get("/search", response=list[ProductSimpleSchema])
def search_products(request: HttpRequest, query: str | None = None):
    products = Product.objects.filter(name__iregex=query)
    return products


@router.get("/{slug}", response=ProductDetailSchema)
def get_product_detail(request: HttpRequest, slug: str):
    product = get_object_or_404(Product, slug=slug)
    return product
