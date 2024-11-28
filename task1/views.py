from .models import Buyer, Game
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


# Представление для главной страницы
def index(request):
    return render(request, 'fourth_task/index.html')

# Представление для магазина
def shop(request):
    games = Game.objects.all()  # Получаем все игры из базы данных
    context = {
        'games': games,
    }
    return render(request, 'fourth_task/page1.html', context)

# Представление для корзины
def cart(request):
    return render(request, 'fourth_task/page2.html')

# Представление для регистрации
def registration_page(request):
    return render(request, 'fifth_task/registration_page.html')
info = {}
def sign_up_by_html(request):
    if request.method == "POST":
        # получаем данные со стороны пользователя:
        name = request.POST.get('name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = int(request.POST.get('age'))

        print(f"'Name' {name}")
        print(f"'password' {password}")
        print(f"'repeat_password' {confirm_password}")
        print(f"'age' {age}")

        # http ответ пользователю
        if password == confirm_password and age >=18:
            buyer_name = Buyer.objects.filter(name=name)
            if buyer_name:
                info['error'] = f'Пользователь {name} уже существует'
                return HttpResponse(f"Ошибка, {info['error']}!")
            Buyer.objects.create(name=name, balance=0, age=age)
            return HttpResponse(f"Приветствуем, {name}!")
        if password != confirm_password:
            info['error'] = 'Пароли не совпадают! Попробуйте еще раз!'
            return HttpResponse(f"Ошибка, {info['error']}!")
        if age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return HttpResponse(f"Ошибка, {info['error']}!")
    # если это Get-запрос:
    return render(request, 'fifth_task/registration_page.html', context=info)


