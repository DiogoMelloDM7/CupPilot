from django.contrib import admin
from .models import Jogador, Comissao, Equipe, Artilharia, Assistente, Tabela, Jogo, Campeonato, Usuario
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(("Meus Campeonatos", {"fields": ("meus_campeonatos",)}))
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Jogador)
admin.site.register(Comissao)
admin.site.register(Equipe)
admin.site.register(Artilharia)
admin.site.register(Assistente)
admin.site.register(Tabela)
admin.site.register(Jogo)
admin.site.register(Campeonato)
admin.site.register(Usuario, UserAdmin)


