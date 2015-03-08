# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.snippets


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150308_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thermostat',
            fields=[
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('serial', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('controls', app.snippets.MultiSelectField(max_length=2, choices=[(b'AC', b'Air Conditioner'), (b'HT', b'Heater')])),
                ('home', models.ForeignKey(to='app.Home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(default=b'OT', max_length=9, choices=[(b'BD', b'Bedroom'), (b'LR', b'Living Room'), (b'KT', b'Kitchen'), (b'BR', b'Bathroom'), (b'HW', b'Hallway'), (b'DR', b'Dining Room'), (b'PR', b'Porch'), (b'PT', b'Patio'), (b'OT', b'Other')]),
            preserve_default=True,
        ),
    ]
