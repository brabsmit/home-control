# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_door_is_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refrigerator',
            name='freezer_set_temp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
