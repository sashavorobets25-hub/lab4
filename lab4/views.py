from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Orphanage, Child


def home_page(request, category_id=None):
    orphanages = Orphanage.objects.all()

    if category_id:
        children = Child.objects.filter(orphanage_id=category_id)
    else:
        children = Child.objects.all()

    context = {
        'orphanages': orphanages,
        'children': children
    }
    return render(request, 'index.html', context)

def child_detail(request, child_id):
    # Шукаємо дитину за ID, або видаємо помилку 404, якщо не знайдено
    child = get_object_or_404(Child, id=child_id)
    orphanages = Orphanage.objects.all()  # Потрібно для відображення меню

    context = {
        'child': child,
        'orphanages': orphanages
    }
    return render(request, 'child_detail.html', context)


def buy_child(request, child_id):
    # Знаходимо дитину за ID
    child = get_object_or_404(Child, id=child_id)

    # Змінюємо статус на "Куплено"
    child.is_purchased = True
    child.save()  # Зберігаємо зміни в базу

    messages.success(request, f"Вітаємо! Ви успішно здійснили покупку: {child.first_name} {child.last_name}.")

    return redirect('home')