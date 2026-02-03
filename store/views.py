from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def product_all(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})