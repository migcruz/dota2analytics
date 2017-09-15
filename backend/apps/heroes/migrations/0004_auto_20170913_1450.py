# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-09-13 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_hero_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='npc_name',
            new_name='localized_name',
        ),
        migrations.AddField(
            model_name='hero',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]