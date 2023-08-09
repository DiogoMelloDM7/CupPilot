# Generated by Django 4.2.2 on 2023-08-08 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0018_remove_equipe_tabela_equipe_tabela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='tabela',
        ),
        migrations.AddField(
            model_name='equipe',
            name='tabela',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tabela_da_equipe', to='campeonato.tabela'),
        ),
    ]
