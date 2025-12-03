from ninja import Schema
import uuid


class IndustrySchema(Schema):
    id: uuid.UUID
    name: str
