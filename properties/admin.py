from django.contrib import admin
from .models import Property

from address.models import AddressField
from address.forms import AddressField as AddressWidget


class PropertyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {'widget': AddressWidget}
    }

admin.site.register(Property, PropertyAdmin)