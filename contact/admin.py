from django.contrib import admin
from contact.models import Contacts, SiteContact


@admin.register(Contacts)
class ContactsModelAdmin(admin.ModelAdmin):
    list_display = ['car_title', 'last_name', 'create_date']

@admin.register(SiteContact)
class SiteContactModelAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'subject']
