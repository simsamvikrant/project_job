# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 15:09
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('got', '0002_remove_king_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='king',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True),
        ),
    ]