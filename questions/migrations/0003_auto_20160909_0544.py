# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 05:44
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models
import questions.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160909_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failurethread',
            name='response',
            field=markdownx.models.MarkdownxField(default=questions.models.FailureThread.response_default),
        ),
    ]
