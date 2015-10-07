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


class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)

    def __unicode__(self):
        return "%s, %s" % (self.user, self.order_date)

    def add_item_to_cart(self, product_id):
        product = Product.objects.get(pk=product_id)
        try:
            preexisting_order = Order.objects.get(product=product, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except Order.DoesNotExist:
            new_order = Order.objects.create(
                product=product,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_item_from_cart(self, product_id):
        product = Product.objects.get(pk=product_id)
        try:
            preexisting_order = Order.objects.get(product=product, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except Order.DoesNotExist:
            pass


class Order(models.Model):
    product = models.ForeignKey(Product)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()

    def __unicode__(self):
        return "%s" % (self.cart)
