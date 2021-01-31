from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    data = {
        'title': 'Home page',
        'values': ['Umid', 'Bahrom', 'Shavkat' ],
        'car': ['BMW', 'Mersades', 'GM'],
        'obj': {'name': 'Umid', 'age':22, 'car':'Tesla'}
    }
    return render(request, 'main/home.html', data)


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')