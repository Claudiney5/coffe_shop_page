from django.contrib import admin

from .models import Product, Client

# registra na aplicação os modelos das Aplicações.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
