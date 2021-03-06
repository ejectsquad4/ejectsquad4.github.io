# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-11 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_clientes', models.ImageField(upload_to='static/img', verbose_name='Logo dos Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='inicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_inico', models.ImageField(upload_to='static/img', verbose_name='Imagem do Inicio')),
            ],
        ),
        migrations.CreateModel(
            name='quem_somos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_quem_somos', models.ImageField(upload_to='static/img', verbose_name='Imagem de Quem Somos')),
                ('desc_quem_somos', models.TextField(verbose_name='Quem Somos')),
            ],
        ),
    ]
