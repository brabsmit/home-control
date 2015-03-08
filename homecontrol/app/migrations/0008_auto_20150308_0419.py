# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.snippets


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150308_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thermostat',
            name='controls',
            field=app.snippets.MultiSelectField(max_length=3, choices=[(b'AC', b'Air Conditioner'), (b'HT', b'Heater'), (b'FN', b'Fan')]),
            preserve_default=True,
        ),
    ]
