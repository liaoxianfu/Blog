# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-12 14:29
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gufeng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article',
            field=ckeditor.fields.RichTextField(max_length=5000, verbose_name='正文'),
        ),
    ]