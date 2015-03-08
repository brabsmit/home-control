# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.snippets


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150308_0419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Refrigerator', max_length=30)),
                ('switch_mode', app.snippets.MultiSelectField(max_length=2, choices=[(b'BN', b'Refrigerator'), (b'VB', b'Freezer')])),
                ('room', models.ForeignKey(to='app.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='door',
            name='name',
            field=models.CharField(default=b'Door', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='light',
            name='name',
            field=models.CharField(default=b'Light', max_length=30),
            preserve_default=True,
        ),
    ]
