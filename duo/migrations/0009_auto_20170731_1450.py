# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-31 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duo', '0008_auto_20170724_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodepowerarchive',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_archive', to='duo.Node'),
        ),
    ]