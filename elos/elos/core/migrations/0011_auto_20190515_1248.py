# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-15 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190511_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviços',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='titulo', max_length=100, verbose_name='Titulo do serviço')),
                ('img_serviço', models.ImageField(upload_to='media/img/img_serviço', verbose_name='Imagem do Serviço')),
                ('desc_serviço', models.TextField(verbose_name='Serviço')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='desc_portfolio',
            field=models.TextField(verbose_name='Portfólio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img_portfolio',
            field=models.ImageField(upload_to='media/img/img_portfolio', verbose_name='Imagem do Portifólio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='titulo',
            field=models.CharField(default='titulo', max_length=100, verbose_name='Titulo do Portifólio'),
        ),
    ]
