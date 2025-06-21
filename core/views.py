from django.shortcuts import render, HttpResponse
from .data import orders

def landing(request):
    """
    Главная страница.
    Отображает шаблон landing.html.
    """
    return render(request, 'landing.html') 

def thanks(request):
    """
    Страница благодарности.
    Отображает шаблон thanks.html.
    """
    return render(request, 'thanks.html') 
def orders_list(request):
    """
    Список заказов.
    Отображает шаблон orders_list.html, передавая данные о заказах.
    """
    context = {'orders': orders}  
    return render(request, 'orders_list.html', context)

def order_detail(request, order_id):
    """
    Страница деталей заказа.
    Отображает шаблон order_detail.html, передавая данные о конкретном заказе.
    Если заказ не найден, возвращает HttpResponse с сообщением об ошибке.
    """
    try:
        # Попытка найти заказ с заданным ID
        order = next(order for order in orders if order['id'] == order_id)
        context = {'order': order}
        return render(request, 'order_detail.html', context)
    except StopIteration:  # Заказ не найден
        return HttpResponse(f'Заказ с id={order_id} не найден')