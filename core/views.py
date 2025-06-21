from django.shortcuts import render, HttpResponse
from .data import orders

# Create your views here.
def landing(request):
    return HttpResponse('<h1>Главная страница<h1>')

def thanks(request):
    return render(request, 'thanks.html')

def orders_list(request):
    return render(request, 'orders_list.html', context=context)

def order_detail(request, order_id):
    order = [order for order in orders if order['id'] == order_id]
    try:
        order = order[0]
        context = {
            'order': order,
            }
    except IndexError:
        return HttpResponse(f'Заказ с id={order_id} не найден')
    else:
        return render(request, 'order_detail.html', context=context)