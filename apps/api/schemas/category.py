import uuid
from datetime import datetime

from ninja import Schema

from .product import ProductSimpleSchema


class CategorySchema(Schema):
    id: uuid.UUID
    name: str
    slug: str
    image: str
    short_description: str
    created_at: datetime
    updated_at: datetime


class CategoryProductSchema(Schema):
    id: uuid.UUID
    name: str
    short_description: str
    products: list[ProductSimpleSchema]
