# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0002_author_blog_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='namexx',
        ),
    ]
