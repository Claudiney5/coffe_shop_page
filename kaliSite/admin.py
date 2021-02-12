from django.contrib import admin

from .models import Product, Client, Order

# registra na aplicação os modelos das Aplicações.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClientAdmin(admin.ModelAdmin):
    list_client = ('nome', 'sobrenome', 'endereco', 'cidade', 'email', 'fone' )

class OrderAdmin(admin.ModelAdmin):
    list_order = ('cliente', 'produto', 'quantidade', 'data', 'email', 'fone' )


admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
admin.site.register(Order)
