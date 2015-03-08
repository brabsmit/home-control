# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150308_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('serial', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('room_type', models.CharField(default=b'OT', max_length=2, choices=[(b'BD', b'Bedroom'), (b'LR', b'Living Room'), (b'KT', b'Kitchen'), (b'BR', b'Bathroom'), (b'HW', b'Hallway'), (b'DR', b'Dining Room'), (b'PR', b'Porch'), (b'PT', b'Patio'), (b'OT', b'Other')])),
                ('home', models.ForeignKey(to='app.Home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='light',
            name='home',
        ),
        migrations.RemoveField(
            model_name='light',
            name='id',
        ),
        migrations.AddField(
            model_name='light',
            name='room',
            field=models.ForeignKey(default=2, to='app.Room'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='light',
            name='serial',
            field=models.IntegerField(default=2, unique=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='light',
            name='name',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
