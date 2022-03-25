from django.contrib import admin
from.models import contact


@admin.register(contact)

class UserAdmin(admin.ModelAdmin):
    list_display=['Name','Email_Address','Text']
