# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-11 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190511_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abc', models.TextField(verbose_name='abc')),
            ],
        ),
    ]
