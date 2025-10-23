from django.contrib import admin
from .models import Eventos

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'organizador')
    search_fields = ('nombre', 'organizador')
    list_filter = ('fecha',)

    class Meta:
        model = Eventos