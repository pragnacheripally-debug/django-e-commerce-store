from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'remove-cart/<int:cart_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'increase/<int:cart_id>/',
        views.increase_quantity,
        name='increase_quantity'
    ),

    path(
        'decrease/<int:cart_id>/',
        views.decrease_quantity,
        name='decrease_quantity'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'place-order/',
        views.place_order,
        name='place_order'
    ),

    path(
        'orders/',
        views.my_orders,
        name='orders'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'
    ),

    path(
        'add-to-wishlist/<int:product_id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),
    path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
),

]