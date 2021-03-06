"""Basico1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from cadastro.views import home
from cadastro.views import listagem
from cadastro.views import nova_transacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('listagem/', listagem),
    path('nova/', nova_transacao, name='urlnova'),
]

admin.site.site_header = 'DTI Teste'