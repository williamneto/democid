# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-12 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('cel', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
