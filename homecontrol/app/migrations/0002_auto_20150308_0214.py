# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
                ('switch_mode', models.CharField(default=b'BN', max_length=2, choices=[(b'BN', b'On/Off'), (b'VB', b'Variable')])),
                ('home', models.ForeignKey(to='app.Home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
    ]
