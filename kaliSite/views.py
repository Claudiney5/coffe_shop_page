from django.shortcuts import render

def index(request):
    context = {
        'produtos': 'Café da manhã',
        'texto': 'poesia funciona bem aqui!'
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
