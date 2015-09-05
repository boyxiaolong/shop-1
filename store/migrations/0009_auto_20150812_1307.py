# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20150808_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(default=b'000000', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.CharField(default=b'-', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(default=b'-', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
