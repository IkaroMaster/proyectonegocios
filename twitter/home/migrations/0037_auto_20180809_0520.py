# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-09 05:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20180809_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguir',
            name='seguidos',
            field=models.ManyToManyField(blank=True, to='home.Perfil'),
        ),
        migrations.AlterField(
            model_name='seguir',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
