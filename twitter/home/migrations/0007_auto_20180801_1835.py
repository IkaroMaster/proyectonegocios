# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-01 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180801_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='portadas',
            new_name='portada',
        ),
    ]