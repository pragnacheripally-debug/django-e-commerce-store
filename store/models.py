from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    stock = models.IntegerField(default=10)

    description = models.TextField()

    image = models.ImageField(
    upload_to='products/',
    blank=True,
    null=True
)

    def __str__(self):
        return self.name


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        default=1
    )

    def __str__(self):
        return self.product.name


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    total = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
class Rating(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    stars = models.IntegerField()

    review = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.product.name} - {self.stars}"
class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name