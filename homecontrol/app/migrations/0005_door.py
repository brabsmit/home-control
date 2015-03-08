# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150308_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('serial', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('locked', models.BooleanField(default=False)),
                ('room', models.ForeignKey(to='app.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
