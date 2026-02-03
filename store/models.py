from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True) # Slug para URL

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='product_creator')
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Renata Dmaria')
    description = models.TextField(blank=True)
    
    # Imagens: Serão salvas na pasta 'media/products/'
    image = models.ImageField(upload_to='products/', default='images/default.png')
    
    # URL do produto: renatadmaria.com.br/vestido-vermelho-g
    slug = models.SlugField(max_length=255)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])