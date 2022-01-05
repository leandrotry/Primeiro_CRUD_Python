from django.shortcuts import render, HttpResponse, render, redirect
from CRUD.forms import PessoaForm
from CRUD.models import Pessoa
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = {}

    def paginar():
        all = Pessoa.objects.all()
        paginator = Paginator(all, 2)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)


    def buscar():
        search = request.GET.get('search')
        opcao = request.GET.get('opcao')
        if search:
            op = opcao
            data['db'] = Pessoa.objects.filter(op=search)
        else:
            return paginar()
    paginar()
    buscar()
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


def view(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk = pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = dict()
    data['db'] = Pessoa.objects.get(pk = pk)
    data['form'] = PessoaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk = pk)
    form = PessoaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Pessoa.objects.get(pk = pk)
    db.delete()
    return redirect('home')

