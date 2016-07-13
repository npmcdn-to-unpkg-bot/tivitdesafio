# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-13 05:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparador', '0002_auto_20160713_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='quantidade_cpu',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantidade de CPU'),
        ),
    ]