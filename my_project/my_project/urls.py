"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from signscape import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signscape.urls')),
    path('faq.html', views.faq_redirect),  
    path('faq/', views.faq, name='faq'),
    path('library/', views.library, name='library'), 
    path('home/', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('levels/', views.levels, name='levels'),
    path('quiz/', views.quiz, name='quiz'),
    path('instructions/', views.instructions, name='instructions'),  
    path('alphabet/', views.alphabet, name='alphabet'),  
    path('travel/', views.travel, name='travel'),
    path('communication/', views.communication, name='communication'),
    path('introduction/', views.introduction, name='introduction'), 
    path('school/', views.school, name='school'), 
    path('friendly/', views.friendly, name='friendly'),    
]