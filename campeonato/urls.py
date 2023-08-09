from django.urls import path, reverse_lazy
from .views import Homepage, HomeLogin, criar_campeonato, Time, CampeonatoPage, MeusCampeonatos, EditCampeonato, CampeonatosMaisVistos, CriarConta, EditarPerfil
from django.contrib.auth import views as auth_views


app_name = 'campeonato'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('cuppilot/', HomeLogin.as_view(), name='homelogin'),
    path('criarcampeonato/', criar_campeonato, name='criar_campeonato'),
    path('detalhesequipe/<int:pk>' ,Time.as_view(), name='detalhes'),
    path('campeonato/<int:pk>', CampeonatoPage.as_view(), name='campeonato_dados'),
    path('meuscampeonatos/', MeusCampeonatos.as_view(), name='meuscampeonatos'),
    path('editcampeonato/<int:pk>', EditCampeonato.as_view(), name='campeonato_edit'),
    path('campeonatosmaisvistos/', CampeonatosMaisVistos.as_view(), name='campeonatosmaisvistos'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage.html'), name='logout'),
    path('editarperfil/<int:pk>', EditarPerfil.as_view(), name='editarperfil'),
    path('mudarsenha/',auth_views.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('campeonato:homelogin')), name='mudarsenha'),
]