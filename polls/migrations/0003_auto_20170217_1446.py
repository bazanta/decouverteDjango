# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170217_1445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReponseQuestion',
            new_name='Reponse',
        ),
    ]