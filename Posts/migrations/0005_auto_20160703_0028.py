# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-02 18:58
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_auto_20160703_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
