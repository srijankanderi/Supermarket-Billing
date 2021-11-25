from rest_framework import serializers
from .models import *


class ItemProductSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField(read_only=True)
    subcategory = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item
        fields = ['name', 'amount', 'subcategory', 'category',]


    def get_category(self, ItemInstance):
        category_name = ItemInstance.subcategory.category.name
        return category_name



    def get_subcategory(self, ItemInstance):
        item_subcategory_name = ItemInstance.subcategory.name
        return item_subcategory_name