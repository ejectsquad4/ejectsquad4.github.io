# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-19 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190518_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviços',
            name='sobre_serviço',
            field=models.TextField(default='Sobre', verbose_name='Descrição aprofundad'),
        ),
        migrations.AlterField(
            model_name='serviços',
            name='desc_serviço',
            field=models.TextField(default='Descrição', verbose_name='Breve descrição'),
        ),
    ]
