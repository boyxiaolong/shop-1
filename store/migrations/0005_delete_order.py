# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20151102_1718'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
