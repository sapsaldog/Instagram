# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20170627_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]