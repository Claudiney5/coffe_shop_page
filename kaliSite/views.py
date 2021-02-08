from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Product


def index(request):
    products = Product.objects.all()    

    if str(request.user) == 'AnonymousUser':
        logado = 'Usuário não logado'
    else: 
        logado = 'Usuário logado'

    context = {
        'products': products,
        'text': 'poesia funciona bem aqui!',
        'logado': logado,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def goods(request, pk):    
    product = get_object_or_404(Product,id=pk) 
    context = {
        'product': product, 
    }
    return render(request, 'product.html', context)

# def error404(request, exception):
#     template = loader.get_template('404.html')
#     return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
