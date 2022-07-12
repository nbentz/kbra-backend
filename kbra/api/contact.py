from ninja import Router

from kbra.schemas import ContactOut, ContactIn
from kbra.models import Contact
from django.db.models import Q
router = Router(tags=["Contacts"])


@router.get("/", response=list[ContactOut])
def get_contacts(request):
    contacts = Contact.objects.all().order_by('last_name', 'first_name')
    return contacts


@router.post("/", response={200: dict, 404: str})
def create_contact(request, payload: ContactIn):
    # checks for unique email.
    if Contact.objects.filter(email=payload.email).exclude(email__isnull=True, email="").exists():
        return 404, "Could not create - duplicate email found, email must be unique."
    if Contact.objects.filter(phone=payload.phone).exclude(phone__isnull=True, phone="").exists():
        return 404, "Could not create - duplicate phone found, phone must be unique."
    try:
        contact = Contact.objects.create(**payload.dict())
        return {"id": contact.id}
    except Exception as e:
        print(e)
        return 404, "Could not create."