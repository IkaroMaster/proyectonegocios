# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-02 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180802_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='usuario',
            new_name='perfil',
        ),
    ]
