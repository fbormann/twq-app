# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171030_1426'),
        ('companies', '0003_company_editors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.User')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='companies.Company')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Team')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
