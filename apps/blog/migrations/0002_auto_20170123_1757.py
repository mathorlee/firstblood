# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u4f5c\u8005', 'verbose_name_plural': '\u4f5c\u8005'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='qq',
            field=models.CharField(max_length=100),
        ),
    ]
