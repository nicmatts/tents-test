# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20151001_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(related_name='subcategories', to='store.Category'),
        ),
    ]
