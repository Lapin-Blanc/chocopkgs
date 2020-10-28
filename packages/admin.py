from django.contrib import admin
from .models import ChocoPackage


class ChocoPackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'software_name', 'software_description', 'selected_by_default']
    list_editable = ['software_name', 'software_description', 'selected_by_default']

    def get_changelist_form(self, request, **kwargs):
        form = super(ChocoPackageAdmin, self).get_changelist_form(request, **kwargs)
        form.base_fields['software_description'].widget.attrs['style'] = 'width: 45em;'
        return form

admin.site.register(ChocoPackage, ChocoPackageAdmin)
