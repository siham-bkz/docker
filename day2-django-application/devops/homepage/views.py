from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return render(request, "homepage/index.html")

def about(request):
        return render(request, "homepage/about.html")

def hello(request):
        return HttpResponse("Hello Django!")
