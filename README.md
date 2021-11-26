Created a supermarket billing project in Django.

![alt text](https://i.pinimg.com/474x/56/75/55/56755529a764cf043208342548438ae9.jpg)

endpoint(s):
{host}/store/items/

allowed_query_params = ['category', 'subcategory', 'name']
sample response:

{
    "name": "Ringfisher",
    "amount": 600,
    "subcategory": "Drinks",
    "category": "Food"
}

sample categories for testing : [Apparel, Electronics, Food, Toys, Cosmetics]
sample subcategories for testing: [Drinks, Mice, Keyboards, Phones]

no pagination/no auth.
