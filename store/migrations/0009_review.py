# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20151108_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_text', models.CharField(default=b'', max_length=1000)),
                ('author', models.CharField(default=b'Anonymous', max_length=30)),
                ('email', models.CharField(default=b'', max_length=30)),
                ('is_shown', models.BooleanField(default=True)),
                ('publication_date', models.DateTimeField(verbose_name=b'date published')),
                ('product', models.ForeignKey(to='store.Product')),
            ],
        ),
    ]
