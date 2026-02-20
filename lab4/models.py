from django.db import models


class Orphanage(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва закладу")
    city = models.CharField(max_length=100, verbose_name="Місто")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return f"{self.name} ({self.city})"

    class Meta:
        verbose_name = "Дитячий будинок"
        verbose_name_plural = "Дитячі будинки"


class Child(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    age = models.PositiveIntegerField(verbose_name="Вік")

    # Додаємо поле ціни (до 10 цифр, 2 після коми)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (грн)")

    orphanage = models.ForeignKey(Orphanage, on_delete=models.CASCADE, verbose_name="Дитячий будинок")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.price} грн"

    class Meta:
        verbose_name = "Дитина"
        verbose_name_plural = "Діти"


class Buyer(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ПІБ покупця")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    # Зв'язуємо покупця з дитиною
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Куплена дитина")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Покупець"
        verbose_name_plural = "Покупці"
