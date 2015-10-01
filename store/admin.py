from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    verbose_name = "Categories"

admin.site.register(Category, CategoryAdmin)
