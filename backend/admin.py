from django.contrib import admin

from .models import VitalData


class VitalDataAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "type",
        "data"
    )


admin.site.register(VitalData, VitalDataAdmin)
