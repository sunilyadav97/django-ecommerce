import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse

def store(request):
    if request.user.is_authenticated:
        customer=request.user
        cart,created=Cart.objects.get_or_create(owner=customer,completed=False)
        cartitems=cart.cartitems_set.all()
    else:
        cart=[]
        cartitems=[]
        cart={'cartquantity':0}

    products=Prodcut.objects.all()
    context={'products':products,'cart':cart,'cartitems':cartitems}

    return render(request,'cart/index.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user
        cart,created=Cart.objects.get_or_create(owner=customer,completed=False)
        cartitems=cart.cartitems_set.all()
    else:
        cart=[]
        cartitems=[]
        cart={'cartquantity':0}
    context={'cartitems':cartitems,'cart':cart}
    return render(request,'cart/cart.html',context)

def checkOut(request):
    return render(request,'cart/checkout.html')

def addToCart(request):
    data=json.loads(request.body)
    product_id=data['product_id']
    action=data['action']
    if request.user.is_authenticated:
        customer=request.user
        product=Prodcut.objects.get(product_id=product_id)
        cart, created=Cart.objects.get_or_create(owner=customer,completed=False)
        cartitems, created=Cartitems.objects.get_or_create(product=product,cart=cart)

        if action=="add":
            cartitems.quantity += 1
        cartitems.save()
        msg={
            'quantity':cart.cartquantity
        }

    return JsonResponse(msg,safe=False)

def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            messages.success(request,'You are logged successfully !')
            return redirect('store')
        else:
            messages.error(request,'Please enter valid username and password')
            return redirect('store')
    else:
        return HttpResponse(' 404 Page not found')


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request,"Your Account has been created successfully!")

        return redirect('store')
    else:
        return HttpResponse(' 404 Page not found ')

def signout(request):
    logout(request)
    messages.success(request,'You are logged out successfully!')
    return redirect('store')

