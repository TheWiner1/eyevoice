# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-02-03 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamimages', '0004_auto_20190203_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamimagemodel',
            name='uri',
            field=models.URLField(blank=True, null=True),
        ),
    ]
