from django.contrib import admin
from .models import Product, Cart, Category, Order, Wishlist, Rating

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Rating)