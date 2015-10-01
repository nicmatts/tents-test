from django.contrib import admin

from .models import Category, Subcategory


class CategoryAdmin(admin.ModelAdmin):
    pass


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
