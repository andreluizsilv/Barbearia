from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome = models.CharField(
        max_length=50,
        choices=[
            ('cliente', 'Cliente'),
            ('gerente', 'Gerente'),
            ('barbeiro', 'Barbeiro'),
            ('recepcionista', 'Recepcionista')
        ],
        unique=True
    )

    def __str__(self):
        return self.get_nome_display()

class Barbearia(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome_completo or self.user.username} ({self.cargo})"
