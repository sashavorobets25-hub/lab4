from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Child, Orphanage, Buyer
from .forms import NewsletterForm, ReviewForm, CheckoutForm
from django.contrib import messages

def home_page(request):
    children = Child.objects.all()
    orphanages = Orphanage.objects.all()

    cart_ids = request.session.get('cart', [])
    cart_items = Child.objects.filter(id__in=cart_ids)

    return render(request, 'index.html', {
        'children': children,
        'orphanages': orphanages,
        'cart_items': cart_items,
        'cart_count': len(cart_ids)
    })

def category_filter(request, orphanage_id):
    orphanage = get_object_or_404(Orphanage, id=orphanage_id)
    children = Child.objects.filter(orphanage=orphanage)
    orphanages = Orphanage.objects.all()

    cart_ids = request.session.get('cart', [])
    cart_items = Child.objects.filter(id__in=cart_ids)

    return render(request, 'index.html', {
        'children': children,
        'orphanages': orphanages,
        'cart_items': cart_items,
        'cart_count': len(cart_ids)
    })

def buy_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    child.is_purchased = True
    child.save()
    messages.success(request, f"Вітаємо! Ви успішно здійснили покупку: {child.first_name} {child.last_name}.")
    return redirect('home')

def child_detail(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    average = child.reviews.aggregate(Avg('rating'))['rating__avg']
    average = round(average, 1) if average else 0

    if request.method == 'POST':
        if 'subscribe' in request.POST:
            sub_form = NewsletterForm(request.POST)
            if sub_form.is_valid():
                sub_form.save()
                return redirect('child_detail', child_id=child.id)

        elif 'review' in request.POST:
            rev_form = ReviewForm(request.POST)
            if rev_form.is_valid():
                new_review = rev_form.save(commit=False)
                new_review.child = child
                new_review.save()
                return redirect('child_detail', child_id=child.id)

    sub_form = NewsletterForm()
    rev_form = ReviewForm()
    orphanages = Orphanage.objects.all()

    cart = request.session.get('cart', [])
    in_cart = str(child.id) in cart

    return render(request, 'child_detail.html', {
        'child': child,
        'orphanages': orphanages,
        'average': average,
        'sub_form': sub_form,
        'rev_form': rev_form,
        'in_cart': in_cart
    })

def add_to_cart(request, child_id):
    cart = request.session.get('cart', [])
    if str(child_id) not in cart:
        cart.append(str(child_id))
        request.session['cart'] = cart
        messages.success(request, "Товар додано в кошик!")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def remove_from_cart(request, child_id):
    cart = request.session.get('cart', [])
    if str(child_id) in cart:
        cart.remove(str(child_id))
        request.session['cart'] = cart
        messages.warning(request, "Товар видалено з кошика.")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_view(request):
    cart_ids = request.session.get('cart', [])
    children_in_cart = Child.objects.filter(id__in=cart_ids)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            buyer_name = form.cleaned_data['full_name']
            buyer_phone = form.cleaned_data['phone']

            for child in children_in_cart:
                Buyer.objects.create(full_name=buyer_name, phone=buyer_phone, child=child)

            request.session['cart'] = []
            messages.success(request, f"Вітаємо, {buyer_name}! Ви успішно оформили замовлення.")
            return redirect('home')
    else:
        form = CheckoutForm()

    return render(request, 'cart.html', {'children': children_in_cart, 'form': form})