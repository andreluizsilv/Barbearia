from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pessoa, Cargo

class UsuarioCreateForm(UserCreationForm):
    nome_completo = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome completo',
            'class': 'form-control'
        }),
        label='Nome completo'
    )
    telefone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '(XX) XXXXX-XXXX',
            'class': 'form-control'
        }),
        label='Telefone'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário (sem espaços)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()  # Agora garantimos que o User será salvo
            nome_completo = self.cleaned_data['nome_completo']
            telefone = self.cleaned_data['telefone']
            cargo_cliente, _ = Cargo.objects.get_or_create(nome='cliente')
            Pessoa.objects.create(
                user=user,
                nome_completo=nome_completo,
                telefone=telefone,
                cargo=cargo_cliente
            )
        return user
