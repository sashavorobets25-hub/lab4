from django.contrib import admin
from .models import Orphanage, Child, Buyer

@admin.register(Orphanage)
class OrphanageAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created_at', 'updated_at')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    # Виводимо ціну в загальний список
    list_display = ('first_name', 'last_name', 'age', 'price', 'orphanage', 'created_at', 'updated_at')

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'child', 'created_at', 'updated_at')