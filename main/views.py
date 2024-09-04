from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'name' : 'Pak Bepe',
        'price': 100000,
        'description': 'Pak Bepe adalah seorang yang sangat baik dan ramah',
        'stock': 67,
    }

    return render(request, "main.html", context)