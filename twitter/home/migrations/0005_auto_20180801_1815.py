# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-01 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180801_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='foto',
        ),
        migrations.AddField(
            model_name='perfil',
            name='portadas',
            field=models.ImageField(default=1, upload_to='portadas'),
            preserve_default=False,
        ),
    ]
