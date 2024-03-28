from django.shortcuts import render,HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth


@has_permission_decorator('cadastrar_avaliador')
def cadastrar_avaliador(request):
    if request.method=="GET":
        return render(request,'cadastrar_avaliador.html')
    if request.method=="POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)

        if user.exists():
            return HttpResponse('Email já cadastrado!')
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo="A")

        return HttpResponse('Avaliador Cadastrado!')
    
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('login'))
        return render(request,'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

    if not user:
        return HttpResponse('Usuário Inválido')
    
    auth.login(request, user)
    return HttpResponse('Usuario logado com sucesso!')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))