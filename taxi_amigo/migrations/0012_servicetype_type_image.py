# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-17 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0011_auto_20170214_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='type_image',
            field=models.ImageField(default=b'', upload_to=b'service_type/images/'),
        ),
    ]
