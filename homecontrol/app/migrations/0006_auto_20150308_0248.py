# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_door'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='door',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='home',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='light',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='room',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='thermostat',
            name='serial',
        ),
        migrations.AddField(
            model_name='door',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=2, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='light',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=3, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=4, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thermostat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=5, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
