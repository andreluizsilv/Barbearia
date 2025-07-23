from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UsuarioCreateForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('agendamentos:servicos')  # Corrigido
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')


@login_required
def servicos(request):
    return render(request, 'cliente/servicos.html')


def cadastro_cliente(request):
    if request.method == 'POST':
        form = UsuarioCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('agendamentos:servicos')
        else:
            messages.error(request, 'Erro no cadastro. Confira os dados e tente novamente.')
    else:
        form = UsuarioCreateForm()

    return render(request, 'cliente/cadastro_cliente.html', {'form': form})
