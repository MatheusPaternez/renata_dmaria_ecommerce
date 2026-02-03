from .basket import Basket

def basket(request):
    # Retorna o carrinho para ser usado em qualquer template html
    return {'basket': Basket(request)}