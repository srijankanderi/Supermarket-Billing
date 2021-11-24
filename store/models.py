from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length= 200)
    category = models.ForeignKey(Category, related_name="subcategoriesInCategory", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):   
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name="itemsInSubcategory", on_delete=models.CASCADE, blank=True, null=True)
    # photo = models.ImageField(upload_to='item_assets')

    def __str__(self):
        return self.name




