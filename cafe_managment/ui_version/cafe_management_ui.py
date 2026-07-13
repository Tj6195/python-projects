import tkinter as tk
from tkinter import font

menu = {
    'Pizza': 200,
    'Burger': 150,
    'Pasta': 180,
    'Salad': 100,
    'Coffee': 50,
    'Juice': 80,
    'Pastry': 120,
}

root = tk.Tk()
root.title("Vini's Café")
root.configure(bg="#f5ede0")
root.geometry("500x800")

title = tk.Label(root, text="☕ Vini's Café", bg="#f5ede0",
                 fg="#4a2c0f", font=("Georgia", 22, "bold"))
title.pack(pady=(20, 4))

subtitle = tk.Label(root, text="freshly made with love",
                    bg="#f5ede0", fg="#9c6e3a", font=("Georgia", 10, "italic"))
subtitle.pack()

#state variable to store the total order amount and cart items
order_total = 0
cart = {}

def add_item(name, price):                                  #func to add item in cart
    global order_total
    order_total += price

    if name in cart:
        cart[name] += 1        # increase quantity by 1
    else:
        cart[name] = 1         # add item with quantity 1

    lines = []
    for name, qty in cart.items():
        lines.append(f"{name} x{qty}")
    cart_label.config(text="\n".join(lines))
    total_label.config(text=f"Total: Rs. {order_total}")

def remove_item():                                           #func to remove item from cart
    global order_total
    if order_total == 0:                                     #condition if cart is already empty
        total_label.config(text="The cart is empty")
    else:
        name = list(cart.keys())[-1]   # get last added item name
        price = menu[name]              # look up its price
        order_total -= price            # subtract from total

        if cart[name] == 1:             # if only 1 left, remove entirely
            del cart[name]
        else:
            cart[name] -= 1             # else just decrease quantity

        if cart:                        # update cart display
            lines = []
            for name, qty in cart.items():
                lines.append(f"{name} x{qty}")
            cart_label.config(text="\n".join(lines))
        else:
            cart_label.config(text="Nothing added yet")

        total_label.config(text=f"Total: Rs. {order_total}")

def clear_cart():                                           #func to clear the cart
    global order_total
    order_total = 0
    cart.clear()
    cart_label.config(text="Nothing added yet")
    total_label.config(text=f"Total: Rs. {order_total}")

tk.Label(root, text="── Menu ──", bg="#f5ede0",
         fg="#9c6e3a", font=("Georgia", 12)).pack(pady=(16, 6))

for item, price in menu.items():
    btn = tk.Button(root, text=f"{item}  •  Rs.{price}",
                    bg="#fff8f0", fg="#4a2c0f",
                    font=("Georgia", 11), relief="flat",
                    bd=0, padx=12, pady=6,
                    command=lambda n=item, p=price: add_item(n, p))
    btn.pack(pady=3, ipadx=10)

tk.Label(root, text="── Your Order ──", bg="#f5ede0",
         fg="#9c6e3a", font=("Georgia", 12)).pack(pady=(16, 4))

cart_label = tk.Label(root, text="Nothing added yet",
                      bg="#f5ede0", fg="#6b4422", font=("Georgia", 11))
cart_label.pack()

total_label = tk.Label(root, text="Total: Rs. 0",
                       bg="#f5ede0", fg="#4a2c0f", font=("Georgia", 13, "bold"))
total_label.pack(pady=6)

def place_order():
    if order_total == 0:
        total_label.config(text="Please select an item first!")
    else:
        total_label.config(text=f"✓ Order placed! Total: Rs. {order_total}")

tk.Button(root, text="Place Order →",                          #ui for place order button
          bg="#4a2c0f", fg="#f5ede0",
          font=("Georgia", 12), relief="flat",
          padx=16, pady=8, command=place_order).pack(pady=8)

tk.Button(root, text="Remove Last Item →",                      #ui for remove item button
          bg="#4a2c0f", fg="#f5ede0",
          font=("Georgia", 12), relief="flat",
          padx=16, pady=8, command=remove_item).pack(pady=8)

tk.Button(root, text="Clear Cart →",                           #ui for clear cart button
          bg="#4a2c0f", fg="#f5ede0",
          font=("Georgia", 12), relief="flat",
          padx=16, pady=8, command=clear_cart).pack(pady=8)

root.mainloop()