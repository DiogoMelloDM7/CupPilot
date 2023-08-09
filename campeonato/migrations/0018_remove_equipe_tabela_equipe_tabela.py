# Generated by Django 4.2.2 on 2023-08-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0017_tabela_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='tabela',
        ),
        migrations.AddField(
            model_name='equipe',
            name='tabela',
            field=models.ManyToManyField(blank=True, null=True, related_name='tabela_da_equipe', to='campeonato.tabela'),
        ),
    ]
