# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20151001_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='slug', populate_from=b'name', editable=False),
            preserve_default=False,
        ),
    ]
