# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sua', '0014_appeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='feedback',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
