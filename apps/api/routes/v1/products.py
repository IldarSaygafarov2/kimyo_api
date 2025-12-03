from ninja import Router
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from apps.api.schemas.product import ProductDetailSchema
from apps.main.models import Product


router = Router(
    tags=["Товары"],
)


@router.get("/{slug}", response=ProductDetailSchema)
def get_product_detail(request: HttpRequest, slug: str):
    product = get_object_or_404(Product, slug=slug)
    return product
