# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150308_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refrigerator',
            name='switch_mode',
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='freezer_current_temp',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='freezer_set_temp',
            field=models.IntegerField(default=36),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='fridge_current_temp',
            field=models.IntegerField(default=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refrigerator',
            name='fridge_set_temp',
            field=models.IntegerField(default=36),
            preserve_default=True,
        ),
    ]
