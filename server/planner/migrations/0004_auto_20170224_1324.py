# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='party',
            name='date_to',
        ),
        migrations.AddField(
            model_name='party',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]