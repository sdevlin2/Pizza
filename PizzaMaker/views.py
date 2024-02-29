from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the pizza index.")

def toppings(request):
    return HttpResponse("These are the toppings.")

def pizza(request):
    return HttpResponse("This is the pizza.")