# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0004_auto_20160518_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('state', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi_amigo.Driver')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi_amigo.TypeService')),
            ],
        ),
    ]
