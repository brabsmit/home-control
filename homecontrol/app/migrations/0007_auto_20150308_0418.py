# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150308_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thermostat',
            name='name',
            field=models.CharField(default=b'Thermostat', max_length=30),
            preserve_default=True,
        ),
    ]
