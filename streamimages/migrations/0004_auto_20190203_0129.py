# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-02-03 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamimages', '0003_auto_20190202_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamimagemodel',
            old_name='scene',
            new_name='scene_id',
        ),
        migrations.RemoveField(
            model_name='streamimagemodel',
            name='img',
        ),
        migrations.AddField(
            model_name='streamimagemodel',
            name='frame',
            field=models.ImageField(blank=True, null=True, upload_to='streamimages/images', verbose_name='img'),
        ),
    ]
