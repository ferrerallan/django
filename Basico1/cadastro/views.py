from django.shortcuts import render

from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    data = {}
    data['now'] = now
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'cadastro/home.html',data)