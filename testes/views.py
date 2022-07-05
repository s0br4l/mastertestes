from django.shortcuts import render
from .forms import MedidasForm, TetesForm
from django.http import HttpResponseRedirect
from .models import Medidasteste

def home(request):
    lista = Medidasteste.objects.all()
    return render(request, 'home.html', {'lista': lista})

def lista(request):
    lista = Medidasteste.objects.all()
    return render(request, 'lista.html', {'lista': lista})

def medidas(request):
    submitted = False
    if request.method == "POST":
        form = MedidasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medidas?submitted=True')
    else:
        form = MedidasForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'medidas.html', {'form': form, 'submitted': submitted})

def testes(request):
    submitted = False
    if request.method == "POST":
        form = TetesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testes?submitted=True')
    else:
        form = TetesForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'testes.html', {'form': form, 'submitted': submitted})

