# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0007_auto_20180714_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postPoster', to=settings.AUTH_USER_MODEL),
        ),
    ]
