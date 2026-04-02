from django.contrib import admin
from .models import Orphanage, Child, Buyer, Subscriber, Review

@admin.register(Orphanage)
class OrphanageAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'created_at', 'updated_at')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'price', 'orphanage', 'created_at', 'updated_at')

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'child', 'created_at', 'updated_at')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('child', 'rating', 'created_at')