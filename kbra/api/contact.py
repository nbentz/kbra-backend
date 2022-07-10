from ninja import Router

from kbra.schemas import ContactOut, ContactIn
from kbra.models import Contact

router = Router(tags=["Contacts"])


@router.get("/", response=list[ContactOut])
def get_contacts(request):
    contacts = Contact.objects.all()
    return contacts


@router.post("/", response={200: dict})
def create_contact(request, payload: ContactIn):
    try:
        contact = Contact.objects.create(**payload)
        return {"id": contact.id}
    except:
        return 404, ""