from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'app_name': 'ZERO',
        'nama_panjang': 'Joe Mathew Rusli',
        'class_name': 'PBP E',

        'name' : 'Ayam Goreng',
        'price': 2000,
        'description': 'Ayam goreng yang enak dan gurih',
        'stock': 65,
    }

    return render(request, "main.html", context)