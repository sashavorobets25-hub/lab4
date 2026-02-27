from django.shortcuts import render
from .models import Orphanage, Child


def home_page(request, category_id=None):
    # Отримуємо всі дитбудинки для меню (хедера)
    orphanages = Orphanage.objects.all()

    # Якщо в меню обрали конкретний дитбудинок, показуємо дітей тільки звідти
    if category_id:
        children = Child.objects.filter(orphanage_id=category_id)
    else:
        # Якщо нічого не обрано - показуємо всіх
        children = Child.objects.all()

    context = {
        'orphanages': orphanages,
        'children': children
    }
    return render(request, 'index.html', context)