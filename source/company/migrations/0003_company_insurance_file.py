# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='insurance_file',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
    ]
