from datetime import datetime

from ninja import Schema
import uuid


class UserRequestCreationSchema(Schema):
    name: str
    phone_number: str
    company: str
    comment: str


class UserRequestSchema(Schema):
    id: uuid.UUID
    name: str
    phone_number: str
    company: str
    comment: str
    created_at: datetime
    updated_at: datetime
