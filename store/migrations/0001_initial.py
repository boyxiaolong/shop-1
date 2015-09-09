# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('brand', models.CharField(default=b'Verana', max_length=100)),
                ('image', models.ImageField(upload_to=b'static/bootstrap/itempics')),
                ('is_active', models.BooleanField(default=True)),
                ('details', models.CharField(default=b'-', max_length=250)),
                ('times_clicked', models.IntegerField(default=0)),
                ('is_recommended', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('is_on_sale', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('volume', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('code', models.CharField(default=b'000000', max_length=50)),
                ('ingredients', models.CharField(default=b'-', max_length=200)),
                ('tags', models.CharField(default=b'-', max_length=200)),
            ],
        ),
    ]
