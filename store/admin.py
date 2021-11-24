from django.contrib import admin
from store.models import *

class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


class StoreSubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    search_fields = ['id', 'name', 'category']


class StoreItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'subcategory']
    search_fields = ['id', 'name', 'amount', 'subcategory']

admin.site.register(Category, StoreCategoryAdmin)
admin.site.register(Subcategory, StoreSubcategoryAdmin)
admin.site.register(Item, StoreItemAdmin)