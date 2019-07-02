from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm

from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    data = {}
    data['lista'] = ['Allan','Sara','Nina']
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'cadastro/home.html',data)

def listagem(request):
    data={}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'cadastro/listagem.html',data)

def nova_transacao(request):
    data = {}
    form=TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return listagem(request)

    data['form'] = form
    return render(request, 'cadastro/form.html',data)