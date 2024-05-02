from django.contrib import admin
from .models import *


class TaomAdmin(admin.ModelAdmin):
    model = Taom
    list_display = ('nom', 'narx')


class IchimlikAdmin(admin.ModelAdmin):
    model = Taom
    list_display = ('nom', 'narx')


admin.site.register(Taom, TaomAdmin)
admin.site.register(Ichimlik, IchimlikAdmin)
