# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.CharField(default=b'-', max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='is_recommended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='times_clicked',
            field=models.IntegerField(default=0),
        ),
    ]
