from django.contrib import admin
from .models import ChocoPackage


class ChocoPackageAdmin(admin.ModelAdmin):
    list_display = ['software_name', 'package_name', 'software_description', 'selected_by_default']

admin.site.register(ChocoPackage, ChocoPackageAdmin)
