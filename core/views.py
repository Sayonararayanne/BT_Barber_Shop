from django.shortcuts import render, redirect
from .models import cliente

def home(request):
    clientes = cliente.objects.all()
    return render(request, "index.html", {"clientes": clientes})

def salvar(request):
    vnome = request.POST.get("nome")
    cliente.objects.create(nome=vnome)
    clientes = cliente.objects.all()
    return render(request, "index.html", {"clientes": clientes})

def editar(request, id):
    vcliente = cliente.objects.get(id=id)
    return render(request, "update.html", {"vcliente": vcliente})
    
    
def update(request, id):
    vnome = request.POST.get("nome")
    vcliente = cliente.objects.get(id=id)
    vcliente.nome = vnome
    vcliente.save()
    return redirect(home)

def deletar(request, id):
    vcliente = cliente.objects.get(id=id)
    vcliente.delete()
    return redirect(home)