# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-02 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moddle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='bike_picture',
            field=models.ImageField(blank=True, upload_to='bikes/'),
        ),
    ]
