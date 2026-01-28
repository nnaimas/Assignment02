from .models import Cart, CartItem, Book

class CartService:
    @staticmethod
    def add_to_cart(cart, book_id, quantity):
        book = Book.objects.get(id=book_id)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
        item.save()

    @staticmethod
    def update_cart_item(item_id, quantity):
        item = CartItem.objects.get(id=item_id)
        item.quantity = quantity
        item.save()
