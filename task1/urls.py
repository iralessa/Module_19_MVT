from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('shop/', views.shop, name='shop'),  # Магазин
    path('cart/', views.cart, name='cart'),  # Корзина
    path('registration/', views.registration_page, name='registration'),  # Страница регистрации
    path('sign-up/', views.sign_up_by_django, name='sign_up'),  # Регистрация с Django формой
    path('sign-up-html/', views.sign_up_by_html, name='sign_up_html'),  # Регистрация с HTML формой

]