from django.contrib import admin
from .models import ChocoPackage


class ChocoPackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'software_name', 'software_description', 'selected_by_default']
    list_editable = ['software_name', 'software_description', 'selected_by_default']

admin.site.register(ChocoPackage, ChocoPackageAdmin)
