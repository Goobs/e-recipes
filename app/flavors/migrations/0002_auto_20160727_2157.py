# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flavors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flavor',
            options={'verbose_name': 'flavor', 'verbose_name_plural': 'flavors'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'review', 'verbose_name_plural': 'reviews'},
        ),
        migrations.AddField(
            model_name='flavor',
            name='sku',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='sku'),
        ),
        migrations.AddField(
            model_name='review',
            name='author_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='author name'),
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='review',
            name='favorite_percentage',
            field=models.FloatField(blank=True, null=True, verbose_name='favorite percentage'),
        ),
    ]
