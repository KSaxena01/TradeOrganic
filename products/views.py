from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic.edit import CreateView
from .forms import CreateProduct

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

class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProduct

    def form_valid(self, form):
        self.object = form.save(commit=True)



