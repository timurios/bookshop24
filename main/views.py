
from django.shortcuts import render, HttpResponse ,  redirect
from products.models import Product
from django.contrib.auth import authenticate, login
from orders.models import Order
from django.contrib.auth.models import User

def main_page(request):
    
    products = None
    if request.method == "POST":
        name = request.POST["name"]
        products = Product.objects.filter(name__contains=name)

    else:
        products = Product.objects.all()
    d = {
        "products": products,
    }
    return render(request, "main/main.html",context=d)

def loginaction(request):
    username = request.POST["username"]
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        return HttpResponse("no user by this username and password")
        return redirect("main_page")
    login(request, user)
    return redirect("main_page")

def profile_page(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    d = {
        "orders": orders,
    }
    return render(request, "main/profile.html", context=d)

def loginpage(request):
    return render(request, "main/login.html")

def contactpage(request):
    return render(request, "main/contact.html")
# Create your views here.
def devpage(request):
    return render(request, "main/dev.html")

def register(request):
    username = request.POST["username"]
    password = request.POST['password']
    email = request.POST["e-mail"]
    if username==None or password==None or email==None:
        return HttpResponse("invalid username or password")
    
    user = User.objects.create_user(username,email,password)
    user.save()
    signup(request, user)
    return redirect("main_page")
    

def regpage(request):
    return render(request,"main/register.html")
    

# def admin(request):
#     return render(request, "main/header.html")
    