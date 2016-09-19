# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 02:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0003_auto_20160917_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi_amigo.Customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='app_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
