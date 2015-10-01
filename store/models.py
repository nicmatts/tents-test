from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category_image = models.ImageField()

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = "Category"


# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     quantity = models.IntegerField(default=1)
#     product_image = models.ImageField()
#     price = models.DecimalField(decimal_places=2, max_digits=8)

#     def __unicode__(self):
#         return "%s" % (self.name)