# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appscan', '0005_user_scan'),
    ]

    operations = [
        migrations.CreateModel(
            name='license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]