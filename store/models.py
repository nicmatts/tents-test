from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category_image = models.ImageField()
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']


class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    subcategory_image = models.ImageField()
    parent_category = models.ForeignKey(Category, related_name="subcategories")
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name_plural = "Subcategories"
        ordering = ['name', 'parent_category']


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    product_image = models.ImageField(blank=True)
    category = models.ManyToManyField(Category)
    subcategory = models.ManyToManyField(Subcategory)
    featured = models.BooleanField(default=False)
    bismarck_weekday_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    bismarck_weekend_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    bismarck_weekly_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    bismarck_4_week_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    forx_weekday_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    forx_weekend_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    forx_weekly_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    forx_4_week_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_25_weekday_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_25_weekend_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_25_weekly_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_25_4_week_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_32_weekday_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_32_weekend_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_32_weekly_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    fargo_32_4_week_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    moorhead_weekday_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    moorhead_weekend_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    moorhead_weekly_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    moorhead_4_week_price = models.DecimalField(decimal_places=2, max_digits=9, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ['name']
