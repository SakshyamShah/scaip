# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_third'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_data',
            name='received_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]