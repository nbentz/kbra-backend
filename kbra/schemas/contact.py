from uuid import UUID
from ninja import Schema


class ContactOut(Schema):
    id: UUID
    first_name: str = None
    last_name: str = None
    phone: str = None
    email: str = None
    address: str = None


class ContactIn(Schema):
    first_name: str = None
    last_name: str = None
    phone: str = None
    email: str = None
    address: str = None
