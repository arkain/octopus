# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octopus', '0003_auto_20180510_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'comment',
            },
        ),
        migrations.AlterModelOptions(
            name='hypothesis',
            options={'verbose_name_plural': 'hypotheses'},
        ),
    ]
