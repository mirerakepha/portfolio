from django.shortcuts import render

def home(request):
    return render(request, 'HOME.html')

def about(request):
    return render(request, 'ABOUT.html')

def portfolio(request):
    return render(request, 'PORTFOLIO.html')

def skills(request):
    return render(request, 'SKILLS.html')

def resume(request):
    return render(request, 'RESUME.html')
