# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='form',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forms.Form'),
            preserve_default=False,
        ),
    ]
