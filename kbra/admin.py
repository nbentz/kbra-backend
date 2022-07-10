from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Contact
admin.site.register(Contact)
