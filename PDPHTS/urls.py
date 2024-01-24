"""
URL configuration for PDPHTS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('welcome/', include("PDPHTS_App.urls")),
    path('login/', include("PDPHTS_App.urls")),
    path('input_login/', include("PDPHTS_App.urls")),
    path('openticket/', include("PDPHTS_App.urls")),
    path('open_ticket/', include("PDPHTS_App.urls")),
    path('active_ticket/', include("PDPHTS_App.urls")),
    path('closed_ticket/', include("PDPHTS_App.urls")),
    path('closeticket/', include("PDPHTS_App.urls")),
    path('close_ticket/', include("PDPHTS_App.urls")),
    path('responder/', include("PDPHTS_App.urls")),
    path('support/', include("PDPHTS_App.urls")),
    path('feedback/', include("PDPHTS_App.urls")),
    path('contact/', include("PDPHTS_App.urls"))
]
