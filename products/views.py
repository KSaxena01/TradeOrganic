from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from django.views.generic.edit import CreateView
from .forms import CreateProduct, UploadForm

def index (request):
    return render(request, 'index.html')

def login (request):
    return render(request, 'login.html')

def register (request):
    return render(request, 'register.html')

def home (request):
    return render(request, 'home.html')

def market (request):
    products = Product.objects.all()
    return render(request, 'market.html', {'products':products})

def about (request):
    return render(request, 'AboutUs.html')

def list (request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    
    return render(request, 'upload.html', {'form' : UploadForm})



