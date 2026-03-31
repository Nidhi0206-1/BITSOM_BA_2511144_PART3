import copy

# --- PROVIDED DATA ---
menu = {
    "Main Course": {
        "Paneer Tikka": {"price": 250.00, "available": True},
        "Butter Chicken": {"price": 320.00, "available": True},
        "Dal Makhani": {"price": 180.00, "available": True}
    },
    "Breads": {
        "Butter Naan": {"price": 40.00, "available": True},
        "Garlic Naan": {"price": 50.00, "available": True}
    },
    "Desserts": {
        "Gulab Jamun": {"price": 60.00, "available": True},
        "Ice Cream": {"price": 80.00, "available": False}
    }
}

inventory = {
    "Paneer Tikka": 10,
    "Butter Chicken": 5,
    "Garlic Naan": 15,
    "Gulab Jamun": 20
}

# Task 1: Menu Explorer
print("--- Restaurant Menu ---")
total_items = 0
available_count = 0
prices = []

for category, items in menu.items():
    print(f"\n[{category}]")
    for name, info in items.items():
        status = "Available" if info["available"] else "Out of Stock"
        # Using :.2f ensures prices look like 180.00 instead of 180.0
        print(f"- {name}: ₹{info['price']:.2f} ({status})")
        
        total_items += 1
        if info["available"]:
            available_count += 1
        prices.append(info["price"])

print(f"\nTotal Items: {total_items}")
print(f"Available Items: {available_count}")
print(f"Budget Friendly (Under ₹150): {len([p for p in prices if p < 150])}")

# Task 2: Cart Operations
def add_to_cart(cart, item_name, qty):
    # Check if item exists in any category
    found_item = None
    for cat in menu:
        if item_name in menu[cat]:
            found_item = menu[cat][item_name]
            break
            
    if not found_item:
        print(f"Error: '{item_name}' is not on the menu.")
        return
    if not found_item["available"]:
        print(f"Error: '{item_name}' is currently unavailable.")
        return
        
    cart[item_name] = cart.get(item_name, 0) + qty
    print(f"Added {qty}x {item_name} to cart.")

def remove_from_cart(cart, item_name):
    if item_name in cart:
        del cart[item_name]
        print(f"Removed {item_name} from cart.")

def update_cart_qty(cart, item_name, new_qty):
    if item_name in cart:
        cart[item_name] = new_qty
        print(f"Updated {item_name} quantity to {new_qty}.")

# Simulation
user_cart = {}
add_to_cart(user_cart, "Paneer Tikka", 1)
add_to_cart(user_cart, "Paneer Tikka", 2) # Merges to 3
add_to_cart(user_cart, "Ice Cream", 1)    # Should fail (unavailable)
add_to_cart(user_cart, "Gulab Jamun", 2)
remove_from_cart(user_cart, "Gulab Jamun")
update_cart_qty(user_cart, "Paneer Tikka", 3)

# Print Bill
print("\n--- Final Bill ---")
subtotal = 0
for item, qty in user_cart.items():
    # Find price again
    price = 0
    for cat in menu:
        if item in menu[cat]:
            price = menu[cat][item]["price"]
    
    item_total = price * qty
    subtotal += item_total
    print(f"{item} x{qty}: ₹{item_total:.2f}")

gst = subtotal * 0.05
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total: ₹{subtotal + gst:.2f}")

# Task 3: Inventory Management
# Create a deep copy for backup
backup_inventory = copy.deepcopy(inventory)

# Deduct from live inventory
print("\n--- Stock Update ---")
for item, qty in user_cart.items():
    if item in inventory:
        inventory[item] -= qty
        print(f"Stock Deducted: {item}. New level: {inventory[item]}")
        
        # Trigger reorder alert (Threshold of 8 for demo purposes)
        if inventory[item] < 8:
            print(f"ALERT: {item} stock is low! Please reorder.")

# Show deep copy works
print(f"\nLive Paneer Tikka Stock: {inventory.get('Paneer Tikka')}")
print(f"Backup Paneer Tikka Stock: {backup_inventory.get('Paneer Tikka')}")
