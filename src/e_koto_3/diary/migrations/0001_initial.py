# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-21 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_text', models.CharField(max_length=25)),
                ('second_text', models.CharField(max_length=25)),
                ('third_text', models.CharField(max_length=25)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
