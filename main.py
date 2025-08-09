class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items in the order.")
            return

        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - Rs.{item.price}")
        print(f"Total: Rs.{self.total()}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Order Confirmed! Thank You.")
            self.items.clear()
        else:
            print("Checkout cancelled.")

# ---------- Main Program ----------
def main():
    menu = [
        Coffee("Cold Coffee", 70),
        Coffee("Cold Coffee with Ice Cream", 100),
        Coffee("Hot Coffee", 30),
        Coffee("Hot Tea", 10),
        Coffee("Masala Tea", 20),
        Coffee("Special Bhai-Bhai Chai", 30)
    ]

    my_order = Order()

    while True:
        print("\n--- Bhai-Bhai Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - Rs.{coffee.price}")

        print(f"{len(menu)+1}. View Order")
        print(f"{len(menu)+2}. Checkout")
        print(f"{len(menu)+3}. Exit")

        choice = input("Choose an option: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menu):
                my_order.add_item(menu[choice-1])
            elif choice == len(menu)+1:
                my_order.show_order()
            elif choice == len(menu)+2:
                my_order.checkout()
            elif choice == len(menu)+3:
                print("Thanks for visiting!")
                break
            else:
                print("Invalid choice.")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
