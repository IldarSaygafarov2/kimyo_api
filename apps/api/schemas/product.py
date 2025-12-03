from ninja import Schema
import uuid


class ProductApplicationSchema(Schema):
    name: str
    description: str


class ProductSimpleSchema(Schema):
    name: str
    slug: str


class ProductDetailSchema(Schema):
    id: uuid.UUID
    name: str
    image: str
    formula: str
    description_1: str | None
    description_2: str | None
    applications: list[ProductApplicationSchema]
