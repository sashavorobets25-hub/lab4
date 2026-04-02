from django import forms
from .models import Subscriber, Review, Buyer

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email...'})
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            # Робимо випадаючий список замість ручного вводу
            'rating': forms.Select(choices=[(i, f"{i} ⭐") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Ваш коментар...'})
        }
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['full_name', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ваш ПІБ'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380...'})
        }