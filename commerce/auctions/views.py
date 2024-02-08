from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, AuctionCategory, Products, Bids, Comments

def addProduct(request):
    products = Products.objects.all()
    if request.method== "POST":
        #Variaveis que vieram da requisição,
        title = request.POST.get("title")
        description = request.POST.get("description")
        startingPrice = request.POST.get("startingPrice")
        category_ids = request.POST.getlist("categories")
        
        #Criação do objeto no banco
        newProduct= Products.objects.create(
            title = title,
            description = description,
            startingPrice = startingPrice,
            
        )
        
         # Obtendo as categorias com base nos IDs fornecidos
        categories = AuctionCategory.objects.filter(id__in=category_ids)
        
        # Atribuindo as categorias ao produto
        newProduct.categories.set(categories)
        
        print(newProduct.id)
        return HttpResponseRedirect(reverse("addProduct"))



        
        
        
    else:
        categories = AuctionCategory.objects.all()
        return render(request, "auctions/addProduct.html", {
            "products": products,
            "categories": categories})

def products_view(request, product_id):
    product = Products.objects.get(pk=product_id)
    return render(request, "auctions/product.html", {
        "product": product,
    })

def index(request):
    products = Products.objects.all()
    return render(request, "auctions/index.html", {
        "products": products,
    })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
