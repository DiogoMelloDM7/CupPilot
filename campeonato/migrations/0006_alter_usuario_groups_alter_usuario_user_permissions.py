# Generated by Django 4.2.4 on 2023-08-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('campeonato', '0005_rename_jogador_artilheiro_artilharia_jogador_artilheiro_campeonato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True,null=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True,null=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
