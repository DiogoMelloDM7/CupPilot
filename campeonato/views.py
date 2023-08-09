from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Equipe, Campeonato, Usuario
from .forms import CriarContaForm

class Homepage(TemplateView):

    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('campeonato:homelogin')
        else:
            return super().get(request, *args, **kwargs)


class HomeLogin(LoginRequiredMixin, TemplateView):
    template_name = 'homelogin.html'


class Time(LoginRequiredMixin, DetailView):
    template_name = "times_dados.html"
    model = Equipe

class CampeonatoPage(LoginRequiredMixin, DetailView):
    template_name = 'campeonato_dados.html'
    model = Campeonato


class EditCampeonato(LoginRequiredMixin, DetailView):
    template_name = 'editcampeonato.html'
    model = Campeonato


class MeusCampeonatos(LoginRequiredMixin, ListView):
    template_name = 'meus_campeonatos.html'
    model = Campeonato


class CampeonatosMaisVistos(LoginRequiredMixin, ListView):
    template_name = "campeonatos_mais_vistos.html"
    model = Campeonato


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def get_success_url(self):
        return reverse('campeonato:login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email', 'username']

    def get_success_url(self):
        return reverse('campeonato:homelogin')


def criar_campeonato(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            nome = request.POST.get('nome')
            numero_times = request.POST.get('numero_times')
            modelo = request.POST.get('modelo')
            ida_volta = request.POST.get('ida_volta')
            cartoes_amarelos = request.POST.get('quant_cartoes')
            tipo_competidor = request.POST.get('competidor')

            campeonato = Campeonato.objects.create(
                organizador=request.user, nome=nome, numero_de_equipes=numero_times, formato=modelo, jogos_ida_e_volta=ida_volta, tipo_competidor=tipo_competidor
            )
            return redirect(reverse('campeonato:campeonato_dados', args=[campeonato.id]))
        return render(request, 'criar_campeonato.html')
    else:
        return redirect('campeonato:homepage')




