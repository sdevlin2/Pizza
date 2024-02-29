from django.http import HttpResponse
from django.shortcuts import render

# from .models import Question

def index(request):
     return render(request, "PizzaMaker/index.html")

def toppings(request):
    return HttpResponse("These are the toppings.")

def pizza(request):
    return HttpResponse("This is the pizza.")