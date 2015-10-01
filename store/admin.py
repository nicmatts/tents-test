from django.contrib import admin

from .models import Category, Subcategory


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
