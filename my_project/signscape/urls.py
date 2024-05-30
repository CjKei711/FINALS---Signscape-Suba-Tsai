from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),
    path('faq.html', views.faq, name='faq'),  
    path('faq/', views.faq, name='faq'),
    path('library.html', views.faq, name='library'),
    path('library/', views.library, name='library'),
    path('game.html', views.game, name='game'),
    path('game/', views.game, name='game'),
    path('levels.html', views.levels, name='levels'),
    path('levels/', views.levels, name='levels'),
    path('quiz.html', views.quiz, name='quiz'),
    path('quiz/', views.quiz, name='quiz'),
    path('instructions.html', views.instructions, name='instructions'),  
    path('instructions/', views.instructions, name='instructions'),
    path('alphabet.html', views.alphabet, name='alphabet'),  
    path('alphabet/', views.alphabet, name='alphabet'),
    path('travel.html', views.travel, name='travel'),  
    path('travel/', views.travel, name='travel'),
    path('communication.html', views.communication, name='communication'),  
    path('communication/', views.communication, name='communication'),
    path('introduction.html', views.introduction, name='introduction'),  
    path('introduction/', views.introduction, name='introduction'),
    path('school.html', views.school, name='school'),  
    path('school/', views.school, name='school'),
    path('friendly.html', views.friendly, name='friendly'),  
    path('friendly/', views.friendly, name='friendly'),
        
        
]