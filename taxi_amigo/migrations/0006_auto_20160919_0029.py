# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 05:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0005_auto_20160918_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktaxi',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_booktaxi_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booktaxi',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_booktaxi_driver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cabride',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_cabride_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cabride',
            name='driver',
            field=models.ForeignKey(blank=True, default=b'1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_cabride_driver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_delivery_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_delivery_driver', to=settings.AUTH_USER_MODEL),
        ),
    ]