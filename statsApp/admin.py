from django.contrib.auth.models import Group, User
from django.contrib import admin
from .models import *


class BuyurtmaTaomAdmin(admin.TabularInline):
    model = BuyurtmaTaom
    extra = 1


class BuyurtmaIchimlikAdmin(admin.TabularInline):
    model = BuyurtmaIchimlik
    extra = 1


class BuyurtmaAdmin(admin.ModelAdmin):
    model = Buyurtma
    inlines = [BuyurtmaTaomAdmin, BuyurtmaIchimlikAdmin]


admin.site.register(Buyurtma, BuyurtmaAdmin)
admin.site.unregister([Group, User])