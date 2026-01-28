from django.db import models
from django.contrib.auth.models import User

# ---------- CUSTOMER ----------
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.user.username


class Address(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='address')
    num = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.num}, {self.street}, {self.city}"


# ---------- BOOK ----------
class Category(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# ---------- CART ----------
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.book.price * item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} x {self.quantity}"
