# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-06 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_chat2_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat2',
            name='perfiles',
        ),
        migrations.AddField(
            model_name='chat2',
            name='perfiles',
            field=models.ManyToManyField(to='home.Perfil'),
        ),
    ]