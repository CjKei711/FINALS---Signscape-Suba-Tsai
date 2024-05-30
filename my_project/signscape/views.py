from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def faq_redirect(request):
    return redirect('home')

def library(request):
    return render(request, 'library.html')

def game(request):
    return render(request, 'game.html')

def levels(request):
    return render(request, 'levels.html')

def quiz(request):
    return render(request, 'quiz.html')

def instructions(request):
    return render(request, 'instructions.html')

def alphabet(request):
    return render(request, 'alphabet.html')

def travel(request):
    return render(request, 'travel.html')

def communication(request):
    return render(request, 'communication.html')

def school(request):
    return render(request, 'school.html')

def introduction(request):
    return render(request, 'introduction.html')

def friendly(request):
    return render(request, 'friendly.html')
