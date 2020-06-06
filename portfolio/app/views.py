from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def portfolio(request):
    return render(request, 'app/portfolio.html')

def project(request):
    return render(request, 'app/project.html')

def blog(request):
    return render(request, 'app/blog.html')

def cv(request):
    return render(request, 'app/cv.html')

def contact(request):
    return render(request, 'app/contact.html')