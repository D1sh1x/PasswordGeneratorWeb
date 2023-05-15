import random

from django.shortcuts import render

def home(request):
    return render(request, 'Generator/home.html')

def about(request):
    return render(request, 'Generator/about.html')

def password(request):
    symbol = list('asdfghjklzxcvbnmqwertyuiop')
    symbol_up = list('ASDFGHJKLZXCVBNMQWERTYUIOP')
    numbers = list('1234567890')
    special_sym = list('~`!@#$%^&*()_-=+{}[]:;"?/.,<>|')
    if request.GET.get('uppercase'):
        symbol.extend(symbol_up)
    if request.GET.get('numbers'):
        symbol.extend(numbers)
    if request.GET.get('special'):
        symbol.extend(special_sym)
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(symbol)
    return render(request, 'Generator/password.html', {"password": thepassword})