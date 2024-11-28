"""
URL configuration for homework_19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1 import views  # Импортируем ваши views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('page1/', views.shop, name='shop'),  # Страница магазина (page1)
    path('page2/', views.cart, name='cart'),  # Страница корзины (page2)
    path('registration/', views.registration_page, name='registration'),  # Страница регистрации
    path('sign_up_by_html/', views.sign_up_by_html, name='sign_up_by_html'),  # Регистрация с Django формой
    #path('sign-up-html/', views.sign_up_by_html, name='sign_up_html'),  # Регистрация с HTML формой
]