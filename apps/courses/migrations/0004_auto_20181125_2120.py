# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-25 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='times',
            new_name='learn_times',
        ),
    ]