from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket

@login_required
def basket_view(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    
    return render(request, 'payment/home.html', {'total': total})