from django.contrib import admin

from .models import Category, Subcategory, Product, Cart, Order, Location


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'slug')
    prepopulated_fields = {"slug": ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'featured')
    prepopulated_fields = {"slug": ('name',)}
    fieldsets = [
        ('Product Information', {'fields': ['name', 'description', 'product_image', 'category', 'subcategory', 'featured', 'slug']}),
        ('Bismarck Prices', {'fields': ['bismarck_weekday_price', 'bismarck_weekend_price', 'bismarck_weekly_price', 'bismarck_4_week_price']}),
        ('Grand Forks Prices', {'fields': ['forx_weekday_price', 'forx_weekend_price', 'forx_weekly_price', 'forx_4_week_price']}),
        ('Fargo 25th Prices', {'fields': ['fargo_25_weekday_price', 'fargo_25_weekend_price', 'fargo_25_weekly_price', 'fargo_25_4_week_price']}),
        ('Fargo 32nd Prices', {'fields': ['fargo_32_weekday_price', 'fargo_32_weekend_price', 'fargo_32_weekly_price', 'fargo_32_4_week_price']}),
        ('Moorhead Prices', {'fields': ['moorhead_weekday_price', 'moorhead_weekend_price', 'moorhead_weekly_price', 'moorhead_4_week_price']}),
    ]


class CartAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Location, LocationAdmin)
