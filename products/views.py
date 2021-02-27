from django.shortcuts import render, redirect
from .models import Product


def list(request):
    products = Product.objects.all()  # [Product1,Product2,Product]
    d = {
        "products": products,
    }
    return render(request, "products/list.html", context=d)


def get(request, id):
    product = Product.objects.get(pk=id)  # Product1 or Product2
    d = {
        "product": product,
    }
    return render(request, "products/get.html", context=d)


def add_page(request):
    return render(request, "products/add.html")


def add_action(request):
    name = request.POST["name"]
    price = int(request.POST["price"])
    description = request.POST["description"]
    genre = request.POST["genre"]
    writer = request.POST["writer"]
    user = request.user
    product = Product(author=user, name=name, price=price, description=description, genre=genre, writer=writer)
    product.save()
    return redirect("product_list")


def remove(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect("product_list")


def update_page(request, id):
    product = Product.objects.get(pk=id)
    d = {
        "product": product,
    }
    return render(request, "products/update.html", context=d)
# Create your views here.
def update_action(request):
    id = int(request.POST["id"])
    name = request.POST["name"]
    price = int(request.POST["price"])
    description = request.POST["description"]
    product = Product.objects.get(pk=id)
    product.name = name
    product.price = price
    product.description = description
    product.save()
    return redirect("product_list")
