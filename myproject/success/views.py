from django.shortcuts import render

# Create your views here.
def car (request):

    return render (request , 'success/car.html')

def game (request):

    return render (request , 'success/game.html')

def product (request):

    return render (request , 'success/product.html')