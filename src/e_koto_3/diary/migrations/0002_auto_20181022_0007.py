# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-22 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Diary',
            new_name='Post',
        ),
    ]