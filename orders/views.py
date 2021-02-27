from django.shortcuts import render, redirect
from products.models import Product
from .models import Order


def make_order(request, id):
    user = request.user
    product = Product.objects.get(pk=id)
    order = Order(user=user, product=product)
    order.save()
    return redirect("main_page")