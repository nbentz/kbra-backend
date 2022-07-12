from django.db import models
import uuid


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, editable=False)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=50, default=None, null=True)
    email = models.CharField(max_length=255, default=None, null=True)
    address = models.TextField(default=None, null=True)