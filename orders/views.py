from django.shortcuts import render
from django.http import JsonResponse
from basket.basket import Basket
from .models import Order, OrderItem

def add(request):
    basket = Basket(request)
    
    if request.POST.get('action') == 'post':
        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=user_id,
                full_name=request.POST.get('full_name'), # Pega o nome digitado
                email=request.POST.get('email'),         # Pega o email digitado
                address1=request.POST.get('address1'),   # Pega o endereço
                address2=request.POST.get('address2'),   # Pega o complemento
                city=request.POST.get('city'),
                post_code=request.POST.get('post_code'),
                total_paid=baskettotal,
                order_key=order_key
            )
            
            # Salva os itens
            for item in basket:
                OrderItem.objects.create(
                    order_id=order.id,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['qty']
                )

        basket.clear()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})