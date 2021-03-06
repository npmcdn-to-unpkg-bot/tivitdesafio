# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-13 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('quantidade_cpu', models.IntegerField(verbose_name='Quantidade de CPU')),
                ('quantidade_memoria', models.IntegerField(verbose_name='Quantidade memoria')),
                ('quantidade_hd', models.IntegerField(verbose_name='Quantidade de HD')),
                ('sistema_operacional', models.CharField(max_length=200, verbose_name='Sistema Operacional')),
                ('preco', models.FloatField(verbose_name='Preco')),
            ],
            options={
                'db_table': 'servidor',
            },
        ),
    ]
