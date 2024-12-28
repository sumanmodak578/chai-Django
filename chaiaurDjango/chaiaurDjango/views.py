from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You are at chai aur Django home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You are at chai aur Django about page")

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Django contact page")