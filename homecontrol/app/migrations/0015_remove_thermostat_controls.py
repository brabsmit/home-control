# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_light_switch_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thermostat',
            name='controls',
        ),
    ]
