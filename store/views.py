from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def product_all(request):
    # Pega todos os produtos ativos
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})

def product_detail(request, slug):
    # Pega um produto específico pelo slug ou retorna erro 404 se não existir
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})