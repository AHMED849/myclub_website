from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html', {})


def executives(request):
    
    context = {}
    return render(request, 'website/executives.html', context)
from django.shortcuts import render

def project_progress(request):
    return render(request, 'website/project_progress.html')

def project_needs(request):
    return render(request, 'website/project_needs.html')

def home(request):
    return render(request, 'website/index.html')