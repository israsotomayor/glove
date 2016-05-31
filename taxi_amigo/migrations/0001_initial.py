# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('born_date', models.DateField(verbose_name=b'fecha de nacimiento')),
                ('user', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('foundation_date', models.DateField(verbose_name=b'fecha de fundacion')),
                ('employee_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi_amigo.Driver')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi_amigo.Enterprise'),
        ),
    ]