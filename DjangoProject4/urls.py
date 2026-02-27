from django.contrib import admin
from django.urls import path
from lab4 import views  # <--- Цього рядка у вас не вистачало
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('category/<int:category_id>/', views.home_page, name='category_filter'),
    path('child/<int:child_id>/', views.child_detail, name='child_detail'),
    path('buy/<int:child_id>/', views.buy_child, name='buy_child'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)