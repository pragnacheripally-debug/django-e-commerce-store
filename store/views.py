from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Cart, Category, Order, Wishlist, Rating


def home(request):
    search = request.GET.get('search')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    if search:
        products = products.filter(
            name__icontains=search
        )

    if category_id:
        products = products.filter(
            category_id=category_id
        )

    categories = Category.objects.all()

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(
            user=request.user
        ).count()
    else:
        cart_count = 0

    return render(
        request,
        'home.html',
        {
            'products': products,
            'categories': categories,
            'cart_count': cart_count
        }
    )


def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    ratings = Rating.objects.filter(
        product=product
    )

    return render(
        request,
        'product_detail.html',
        {
            'product': product,
            'ratings': ratings
        }
    )

def add_to_cart(request, product_id):

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    product = Product.objects.get(id=product_id)

    cart_item = Cart.objects.filter(
        user=request.user,
        product=product
    ).first()

    if cart_item:

        cart_item.quantity += 1
        cart_item.save()

    else:

        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

    return redirect('/')


def cart(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    carts = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in carts:
        total += (
            item.product.price *
            item.quantity
        )

    return render(
        request,
        'cart.html',
        {
            'carts': carts,
            'total': total
        }
    )


def remove_from_cart(request, cart_id):
    cart = Cart.objects.get(
        id=cart_id
    )

    cart.delete()

    return redirect('/cart/')


def register(request):

    if request.method == 'POST':

        form = UserCreationForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                '/accounts/login/'
            )

    else:

        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )
def place_order(request):

    carts = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in carts:
        total += (
            item.product.price *
            item.quantity
        )

    Order.objects.create(
        user=request.user,
        total=total
    )

    carts.delete()

    return redirect('/orders/')
def increase_quantity(request, cart_id):

    cart = Cart.objects.get(id=cart_id)

    cart.quantity += 1
    cart.save()

    return redirect('/cart/')


def decrease_quantity(request, cart_id):

    cart = Cart.objects.get(id=cart_id)

    if cart.quantity > 1:

        cart.quantity -= 1
        cart.save()

    else:

        cart.delete()

    return redirect('/cart/')
def checkout(request):

    carts = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in carts:
        total += item.product.price * item.quantity

    return render(
        request,
        'checkout.html',
        {
            'total': total
        }
    )
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        'orders.html',
        {
            'orders': orders
        }
    )
def profile(request):

    orders = Order.objects.filter(
        user=request.user
    )

    total_spent = 0

    for order in orders:
        total_spent += order.total

    return render(
        request,
        'profile.html',
        {
            'orders_count': orders.count(),
            'total_spent': total_spent
        }
    )
def add_to_wishlist(request, product_id):

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    product = Product.objects.get(
        id=product_id
    )

    wishlist_item = Wishlist.objects.filter(
        user=request.user,
        product=product
    ).first()

    if not wishlist_item:

        Wishlist.objects.create(
            user=request.user,
            product=product
        )

    return redirect('/')


def wishlist(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    items = Wishlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        'wishlist.html',
        {
            'items': items
        }
    )
def dashboard(request):

    total_products = Product.objects.count()

    total_orders = Order.objects.count()

    total_users = User.objects.count()

    total_revenue = 0

    orders = Order.objects.all()

    for order in orders:
        total_revenue += order.total

    return render(
        request,
        'dashboard.html',
        {
            'total_products': total_products,
            'total_orders': total_orders,
            'total_users': total_users,
            'total_revenue': total_revenue
        }
    )