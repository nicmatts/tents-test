# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20151001_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=b'default-slug'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default=b'default-slug'),
        ),
    ]
