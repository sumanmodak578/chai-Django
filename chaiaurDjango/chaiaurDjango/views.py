from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You are at chai aur Django home page")

def about(request):
    return HttpResponse("Hello, world. You are at chai aur Django about page")

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Django contact page")