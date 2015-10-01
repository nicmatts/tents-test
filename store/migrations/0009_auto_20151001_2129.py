# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20151001_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, unique=True, populate_from=b'name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, unique=True, populate_from=b'name'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, unique=True, populate_from=b'name'),
        ),
    ]
