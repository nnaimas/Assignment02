from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart, Customer
from .services import CartService
from django.contrib.auth.decorators import login_required


def book_list(request):
    books = Book.objects.all()
    return render(request, 'shop/book_list.html', {'books': books})


@login_required
def add_to_cart(request, book_id):
    customer = Customer.objects.get(user=request.user)
    cart, _ = Cart.objects.get_or_create(customer=customer)

    CartService.add_to_cart(cart, book_id, 1)
    return redirect('view_cart')


@login_required
def view_cart(request):
    customer, created = Customer.objects.get_or_create(
    user=request.user,
    defaults={'email': request.user.email})
    cart = Cart.objects.filter(customer=customer).first()
    return render(request, 'shop/cart.html', {'cart': cart})
