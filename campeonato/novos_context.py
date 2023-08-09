from .models import Campeonato
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


def lista_campeonatos_usuario(request):
    try:
        user = request.user
        lista_campeonatos = Campeonato.objects.filter(organizador=user).order_by("visualizacoes")
        return {"lista_campeonatos":lista_campeonatos}
    except:
        lista_campeonatos = []
        return {"lista_campeonatos": lista_campeonatos}
    
def campeonatos_mais_vistos(request):
    lista_campeonatos_mais_vistos = Campeonato.objects.all().order_by("visualizacoes")
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
