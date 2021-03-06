# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 10:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import moddle.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=20)),
                ('bike_gender', models.CharField(max_length=16)),
                ('bike_age', models.CharField(max_length=16)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('bike_picture', models.ImageField(blank=True, upload_to=moddle.models.get_bike_image_folder)),
                ('price_per_day', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('bikeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moddle.Bike')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(blank=True, max_length=512)),
                ('phone_number', models.CharField(blank=True, max_length=16)),
                ('gender', models.CharField(max_length=16)),
                ('post_code', models.CharField(max_length=7)),
                ('longitude', models.FloatField(blank=True, default=-4.2924705147743225, null=True)),
                ('latitude', models.FloatField(blank=True, default=55.87371280304047, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to=moddle.models.get_user_image_folder)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to='moddle.UserProfile'),
        ),
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='moddle.UserProfile'),
        ),
        migrations.AddField(
            model_name='bike',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moddle.UserProfile'),
        ),
    ]
