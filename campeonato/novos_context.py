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
        lista_das_equipes = [time.nome for time in camp.equipes_campeonato.all()]
        quant_times = len(lista_das_equipes)
        rodadas = {}
        confrontos = list(combinations(lista_das_equipes, 2))
        
        jogos_por_rodada = quant_times // 2
        
        for rodada_num in range(1, quant_times):
            rodada_jogos = []
            times_na_rodada = set()

            while len(rodada_jogos) < jogos_por_rodada:
                jogo = None

                for confronto in confrontos:
                    time1, time2 = confronto

                    if time1 not in times_na_rodada and time2 not in times_na_rodada:
                        jogo = f'{time1} X {time2}'
                        break

                if jogo:
                    rodada_jogos.append(jogo)
                    times_na_rodada.add(time1)
                    times_na_rodada.add(time2)
                    confrontos.remove((time1, time2))

            rodadas[f'rodada{rodada_num}'] = rodada_jogos

        return {"rodadas": rodadas}
    except:
        rodadas = {}
        return {"rodadas": rodadas}

