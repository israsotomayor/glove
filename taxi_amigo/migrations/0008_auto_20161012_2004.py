# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0007_auto_20161008_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktaxi',
            name='destination_address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='booktaxi',
            name='destination_latitude',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='booktaxi',
            name='destination_longitude',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='booktaxi',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='coupon',
            name='coupon_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='delivery',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]