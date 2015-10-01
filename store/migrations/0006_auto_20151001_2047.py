# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20151001_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=1)),
                ('product_image', models.ImageField(upload_to=b'', blank=True)),
                ('bismarck_weekday_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('bismarck_weekend_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('bismarck_weekly_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('bismarck_4_week_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('forx_weekday_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('forx_weekend_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('forx_weekly_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('forx_4_week_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_25_weekday_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_25_weekend_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_25_weekly_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_25_4_week_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_32_weekday_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_32_weekend_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_32_weekly_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('fargo_32_4_week_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('moorhead_weekday_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('moorhead_weekend_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('moorhead_weekly_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('moorhead_4_week_price', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['name', 'parent_category'], 'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='store.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(to='store.Subcategory'),
        ),
    ]
