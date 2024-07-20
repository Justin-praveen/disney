from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
import signal
import time
from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.

def home(request):
    category=Category.objects.all()
    new_arrival=New_Arrival.objects.all()
    

  
    return render(request,'home.html',{'category':category,'new_arrival':new_arrival})

def product(request,name):

    if name:
        category=Category.objects.get(name=name)
        product=Product.objects.filter(key=category).order_by('-id')
        return render(request,'productspage.html', {'product':product})
    
def product_details(request,code):
 
    if code:
        product=Product.objects.filter(p_code=code)
        
        return render(request,'productdetails.html', {'product':product})
    

def log(request):
    if request.method=='POST':
        name=request.POST.get('username')
        word=request.POST.get('password')
        
        user = authenticate(request, username=name, password=word)
        if user is not None:
            
            return redirect('home')  # Replace 'dashboard' with your desired redirect URL after successful login
        else:
            messages.error(request, 'Invalid username or password.')

    return render (request, 'login.html')


def handler(signum, frame):
    raise TimeoutError("Timed out!")

def cartadd(request,code):
    
    if code:
        data=Product.objects.get(p_code=code)
        code=data.p_code
        name=data.product_name
        price=data.new_price
        image=data.product_image
        cart=Cart(
            p_code=code,
            name=name,
            username="just",
            price=price,
            image=image,
            )
        cart.save()

        time.sleep(3)  # Simulate a long operation
        return redirect('home')
        
    
    
def cart(request):
    cart=Cart.objects.all().order_by('-id')
    
    return render(request,'cart.html',{'cart':cart})

def faq(request):
    faq=FAQ.objects.all().order_by('-id')

    return render(request,'faq.html',{'faq':faq})

  
def product_details(request,code):
 
    if code:
        product=New_Arrival.objects.filter(p_code=code)
     
        return render(request,'productdetails.html', {'product':product})
    
def order (request,code):
    if code:

        data=Product.objects.get(p_code=code)
        code=data.p_code
        name=data.product_name
        image=data.product_image
        username="just"

        order=Orders(
            p_code=code,
            name=name,
            image=image,
            username=username
        )
        order.save()
        time.sleep(3)
        return redirect('cart')

def about (request):
    return render (request, 'about.html')