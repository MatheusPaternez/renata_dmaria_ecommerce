from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from store.models import Product
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})

def basket_add(request):
    basket = Basket(request)
    
    # Verifica se a requisição é POST (segurança)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        
        product = get_object_or_404(Product, id=product_id)
        
        # Adiciona no carrinho
        basket.add(product=product, qty=product_qty)

        # Retorna a nova quantidade total para atualizar o ícone
        response = JsonResponse({'qty': basket.__len__()})
        return response
    pass

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        
        response = JsonResponse({'qty': basket.__len__(), 'subtotal': basket.get_total_price()})
        return response
    
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        
        basket.update(product=product_id, qty=product_qty)
        
        response = JsonResponse({'qty': basket.__len__(), 'subtotal': basket.get_total_price()})
        return response