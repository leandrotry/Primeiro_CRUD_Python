from django.shortcuts import render, HttpResponse, render, redirect
from CRUD.forms import PessoaForm
from CRUD.models import Pessoa


# Create your views here.

def home(request):
    data = {}
    data['db'] = Pessoa.objects.all()

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = PessoaForm
    return render(request, 'form.html', data)

def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')