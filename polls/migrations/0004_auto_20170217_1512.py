# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170217_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='nom',
            field=models.CharField(default='Anonyme', max_length=50),
        ),
    ]
