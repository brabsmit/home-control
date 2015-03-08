# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150308_0429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='door',
            old_name='locked',
            new_name='is_locked',
        ),
        migrations.AddField(
            model_name='light',
            name='is_on',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thermostat',
            name='current_temp',
            field=models.IntegerField(default=72),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thermostat',
            name='set_temp',
            field=models.IntegerField(default=72),
            preserve_default=False,
        ),
    ]
