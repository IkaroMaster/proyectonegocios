# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-07 22:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_chat2_ultimo_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='emisor',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='receptor',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
