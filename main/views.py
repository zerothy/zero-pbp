import datetime
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product, FeaturedProduct
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import bleach

@login_required(login_url='main:login')
def show_main(request):
    featured_product = FeaturedProduct.objects.filter(product__user=request.user)

    context = {
        'username': request.user.username,
        'featured_product': featured_product,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = bleach.clean(request.POST.get('name'), strip=True, tags=[], attributes={})
    price = bleach.clean(request.POST.get('price'), strip=True, tags=[], attributes={})
    description = bleach.clean(request.POST.get('description'), strip=True, tags=[], attributes={})
    stock = bleach.clean(request.POST.get('stock'), strip=True, tags=[], attributes={})
    user = request.user

    if not name:
        return JsonResponse({'status': 'ERROR', 'message': 'Name is required.'}, status=400)
    if not price:
        return JsonResponse({'status': 'ERROR', 'message': 'Price is required.'}, status=400)
    if not description:
        return JsonResponse({'status': 'ERROR', 'message': 'Description is required.'}, status=400)
    if not stock:
        return JsonResponse({'status': 'ERROR', 'message': 'Stock is required.'}, status=400)

    new_product = Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        user=user,
    )
    new_product.save()

    return JsonResponse({'status': 'CREATED'}, status=201)

def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Invalid username or password.')
   else:
        form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(request, id):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(request, id):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')