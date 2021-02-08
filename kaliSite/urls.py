from django.urls import path
from .views import index, contact, goods

urlpatterns = [

    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('product/<int:pk>', goods, name='product'),

]