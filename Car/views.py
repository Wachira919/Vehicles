from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("")

# def about(request):
#     return HttpResponse("<h1> About Page</h1>")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')