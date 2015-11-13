# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='publication_date',
            new_name='date_published',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
    ]
