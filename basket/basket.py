from store.models import Product

class Basket():
    """
    Uma classe base para o carrinho de compras (session padrão)
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey') # Tenta pegar a sessão existente
        
        if 'skey' not in request.session: # Se não existir, cria uma nova
            basket = self.session['skey'] = {}
            
        self.basket = basket

    def add(self, product, qty):
        """
        Adiciona um produto ao carrinho ou atualiza a quantidade.
        """
        product_id = str(product.id)

        # Se o produto já existe no carrinho, SOMAMOS a nova quantidade
        if product_id in self.basket:
            self.basket[product_id]['qty'] += int(qty)
            
        # Se não existe, criamos um novo
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
        self.session.modified = True

    def __len__(self):
        """
        Conta a quantidade de itens no carrinho (para o ícone do menu).
        """
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        """
        Coleta os IDs da sessão e busca os produtos no banco de dados
        para entregar tudo pronto para o template.
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def get_total_price(self):
        return sum(float(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        """
        Remove um item da sessão.
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True

    def update(self, product, qty):
        """
        Atualiza a quantidade de um item.
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
            self.session.modified = True

    def clear(self):
        """
        Remove o carrinho da sessão.
        """
        # Deleta a chave 'skey' da sessão
        del self.session['skey']
        self.session.modified = True