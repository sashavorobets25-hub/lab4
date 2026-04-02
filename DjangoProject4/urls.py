from django.contrib import admin
from django.urls import path
from lab4 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('category/<int:orphanage_id>/', views.category_filter, name='category_filter'),
    path('child/<int:child_id>/', views.child_detail, name='child_detail'),
    path('buy/<int:child_id>/', views.buy_child, name='buy_child'),
    path('add-to-cart/<int:child_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:child_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('Subscriber/<int:sub_id>/', views.child_detail, name='subcription'),
    path('Review/<int:review_id>/', views.child_detail, name='review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)