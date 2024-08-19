from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = [
        {'name': 'Киберпук', 'price': 100},
        {'name': 'Ган-Банг', 'price': 200},
        {'name': 'Нет Фор Соль', 'price': 300},
    ]
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')