from django.urls import path
from . import views

app_name = 'agendamentos'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('servicos/', views.servicos, name='servicos'),
    path('cadastro/', views.cadastro_cliente, name='cadastro_cliente'),

]
