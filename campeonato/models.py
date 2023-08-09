from django.db import models
from django.contrib.auth.models import AbstractUser


class Jogador(models.Model):
    equipe = models.ForeignKey("Equipe", related_name="jogador", on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    posicao = models.CharField(max_length=30)
    data_nascimento = models.DateField(blank=True, null=True)
    numero = models.IntegerField()
    gols = models.IntegerField(blank=True, null=True)
    assistencias = models.IntegerField(blank=True, null=True)
    RG_CPF = models.CharField(max_length=15)

    def __str__(self):
        return self.nome + " - " + self.equipe.nome


class Comissao(models.Model):
    equipe = models.ForeignKey("Equipe", related_name="equipe_da_comissao", on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(blank=True, null=True)
    RG_CPF = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    tabela = models.ForeignKey("Tabela", related_name="tabela_da_equipe", blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    quant_atletas = models.IntegerField()
    pontos = models.IntegerField(blank=True, null=True, default=0)
    jogos = models.IntegerField(blank=True, null=True, default=0)
    gols_feitos = models.IntegerField(blank=True, null=True, default=0)
    gols_sofridos = models.IntegerField(blank=True, null=True, default=0)
    cartoes_amarelos = models.IntegerField(blank=True, null=True, default=0)
    cartoes_vermelhos = models.IntegerField(blank=True, null=True, default=0)
    vitorias = models.IntegerField(blank=True, null=True, default=0)
    empates = models.IntegerField(blank=True, null=True, default=0)
    derrotas = models.IntegerField(blank=True, null=True, default=0)
    aproveitamento = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.nome + " - " + self.tabela.campeonato.nome


class Artilharia(models.Model):
    jogador_artilheiro_campeonato = models.ManyToManyField("Jogador")
    tabela = models.ForeignKey("Tabela", related_name="artilheiros", on_delete=models.CASCADE,blank=True, null=True)
    gols = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.tabela


class Assistente(models.Model):
    jogador_assistente_campeonato = models.ManyToManyField("Jogador")
    tabela = models.ForeignKey("Tabela", related_name="assistentes", on_delete=models.CASCADE, blank=True, null=True)
    assistencias = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.tabela


class Tabela(models.Model):
    campeonato = models.ForeignKey("Campeonato", related_name="tabela_do_campeonato", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.campeonato.nome


class Jogo(models.Model):
    equipe_mandante = models.ForeignKey("Equipe", related_name="mandante", on_delete=models.CASCADE)
    equipe_visitante = models.ForeignKey("Equipe", related_name="visitante", on_delete=models.CASCADE)
    placar = models.CharField(max_length=30, blank=True, null=True)
    jogador_marcador_jogo = models.ManyToManyField("Jogador", related_name="marcador_no_jogo", blank=True, null=True)
    jogador_assistente_jogo = models.ManyToManyField("Jogador", related_name="passador_no_jogo", blank=True, null=True)
    cartoes_amarelos = models.IntegerField(blank=True, null=True)
    cartoes_vermelhos = models.IntegerField(blank=True, null=True)
    horario = models.CharField(max_length=30, blank=True, null=True)
    local = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.equipe_mandante + " X " + self.equipe_visitante


class Campeonato(models.Model):
    organizador = models.ForeignKey("Usuario", related_name="organizador", on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    numero_de_equipes = models.IntegerField()
    formato = models.CharField(max_length=30)
    visualizacoes = models.IntegerField(default=0, blank=True, null=True)
    jogos_ida_e_volta = models.CharField(max_length=5)
    tipo_competidor = models.CharField(max_length=30)

    def __str__(self):
        return self.nome




class Usuario(AbstractUser):
    meus_campeonatos = models.ManyToManyField("Campeonato", related_name="meus_campeonatos", null=True)
    #groups = models.ManyToManyField("auth.Group", related_name="usuarios")
    #user_permissions = models.ManyToManyField("auth.Permission", related_name="usuarios")

