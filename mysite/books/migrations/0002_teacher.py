# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-05 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=50)),
            ],
        ),
    ]
