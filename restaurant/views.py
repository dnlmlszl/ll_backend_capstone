from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    pass

def book(request):
    pass

def menu(request):
    pass

def display_menu_item(request):
    pass