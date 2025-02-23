class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        """Calculate the total price for this item."""
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_cart_item(self, item):
        self.items.append(item)
        
    def remove_cart_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = sum(item.calculate_total() for item in self.items)
        return total

    def display_cart(self):
        if not self.items:
            print("The cart is empty.")
            return
        print("Items in the cart:")
        for item in self.items:
            print(f"{item.item_name}: ${item.price} x {item.quantity} = ${item.calculate_total()}")

if __name__ == "__main__":
    cart = ShoppingCart()

    item1 = CartItem("Shoes", 500, 2)
    item2 = CartItem("Shirt", 100, 4)

    cart.add_cart_item(item1)
    cart.add_cart_item(item2)
    cart.display_cart()
    
    print("_"*25)
    total = cart.calculate_total()
    print(f"Total cost: ${total:.2f}")