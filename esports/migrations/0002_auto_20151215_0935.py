# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('BENCH', 'BENCH'), ('RETIRED', 'RETIRED'), ('STREAMER', 'STREAMER')], max_length=20),
        ),
    ]