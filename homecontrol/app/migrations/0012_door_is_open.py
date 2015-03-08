# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150308_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='is_open',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
