from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def services(request):
    """A view that displays the services page"""
    return render(request, "services.html")
