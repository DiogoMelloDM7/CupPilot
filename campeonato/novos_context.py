from django.shortcuts import get_object_or_404
from .models import Campeonato, Equipe
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


def lista_campeonatos_usuario(request):
    try:
        if request.user.is_authenticated:
            user = request.user
            lista_campeonatos = Campeonato.objects.filter(organizador=user).order_by("-visualizacoes")
            return {"lista_campeonatos":lista_campeonatos}
    except:
        lista_campeonatos = []
        return {"lista_campeonatos": lista_campeonatos}
    
def campeonatos_mais_vistos(request):
    try:
        lista_campeonatos_mais_vistos = Campeonato.objects.all().order_by("-visualizacoes")
        return {"campeonatos_vistos": lista_campeonatos_mais_vistos}
    except:
        return {"campeonatos_vistos": lista_campeonatos_mais_vistos}


class EmailOrUsernameBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(Q(username__exact=username) | Q(email__exact=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None


def geracaoDosJogos(request):
    try:
        from itertools import combinations
        pk = int(request.path.split('/')[-1])
        camp = get_object_or_404(Campeonato, id=pk)
        lista_das_equipes = []
        quant_times = 0
        rodadas = {}
        for time in camp.equipes_campeonato.all():
            lista_das_equipes.append(time.nome)
            quant_times += 1
        confrontos = list(combinations(lista_das_equipes, 2))
        for c in range(1, quant_times):
            confrontos_copy = confrontos.copy()
            jogos_na_rodada = []
            times_jogados = set()

            while confrontos_copy and len(jogos_na_rodada) < quant_times // 2:
                jogo = confrontos_copy.pop(0)
                time1, time2 = jogo

                if time1 not in times_jogados and time2 not in times_jogados:
                    jogo = time1 + " X " + time2
                    jogos_na_rodada.append(jogo)
                    times_jogados.add(time1)
                    times_jogados.add(time2)

            rodadas[f'Rodada {c}'] = jogos_na_rodada
            confrontos = [c for c in confrontos if c not in jogos_na_rodada]
        

        return {"rodadas": rodadas}
    except:
        rodadas = {}
        return {"rodadas": rodadas}
