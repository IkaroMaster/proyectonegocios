# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-02 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180802_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='Multimedia',
            field=models.ImageField(blank=True, null=True, upload_to='foto_tweet'),
        ),
    ]
