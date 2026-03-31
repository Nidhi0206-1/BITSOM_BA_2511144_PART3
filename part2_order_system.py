import sys
import copy

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# --- Provided Data ---
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# ======================================================================
# Task 1 - Explore the Menu
# ======================================================================
print("Task 1: Explore the Menu\n")

# finding all categories manually
categories_list = []
for item in menu:
    cat = menu[item]["category"]
    if cat not in categories_list:
        categories_list.append(cat)

for c in categories_list:
    print(f"===== {c} =====")
    for item in menu:
        if menu[item]["category"] == c:
            price = menu[item]["price"]
            avail = menu[item]["available"]
            if avail == True:
                status = "[Available]"
            else:
                status = "[Unavailable]"
            
            # basic padding so it looks like a student wrote it
            padded_item = item.ljust(16, " ")
            print(f"{padded_item} ₹{price}   {status}")
    print() # blank line

total_items = len(menu)
available_count = 0
for item in menu:
    if menu[item]["available"] == True:
        available_count += 1

highest_price = 0
most_expensive_item = ""

under_150_items = []

for item in menu:
    p = menu[item]["price"]
    if p > highest_price:
        highest_price = p
        most_expensive_item = item
        
    if p < 150:
        under_150_items.append(item + " (₹" + str(p) + ")")

print(f"Total number of items on menu: {total_items}")
print(f"Total number of available items: {available_count}")
print(f"The most expensive item: {most_expensive_item} (₹{highest_price})")

print("Items priced under ₹150:")
for u_item in under_150_items:
    print(" - " + u_item)


# ======================================================================
# Task 2 - Cart Operations
# ======================================================================
print("\n\nTask 2: Cart Operations\n")

cart = []

def add_to_cart(item_name, qty):
    # checking if it exists
    if item_name not in menu:
        print(f"Cannot add: '{item_name}' does not exist in the menu.")
        return
        
    # check if available
    if menu[item_name]["available"] == False:
        print(f"Cannot add: '{item_name}' is currently unavailable.")
        return
        
    # check if already in cart
    found_in_cart = False
    for c_item in cart:
        if c_item["item"] == item_name:
            c_item["quantity"] = c_item["quantity"] + qty
            found_in_cart = True
            
    # if not in cart, add fresh
    if found_in_cart == False:
        new_entry = {
            "item": item_name,
            "quantity": qty,
            "price": menu[item_name]["price"]
        }
        cart.append(new_entry)
    
    print(f"Added {qty}x '{item_name}' to cart.")

def remove_from_cart(item_name):
    # finding index manually
    idx_to_remove = -1
    for i in range(len(cart)):
        if cart[i]["item"] == item_name:
            idx_to_remove = i
            
    if idx_to_remove != -1:
        del cart[idx_to_remove]
        print(f"Removed '{item_name}' from cart.")
    else:
        print(f"Cannot remove: '{item_name}' is not in your cart.")

# simulating instructions
add_to_cart("Paneer Tikka", 2)
print("Cart state:", cart)

add_to_cart("Gulab Jamun", 1)
print("Cart state:", cart)

add_to_cart("Paneer Tikka", 1)  # should update to 3
print("Cart state:", cart)

add_to_cart("Mystery Burger", 1)
print("Cart state:", cart)

add_to_cart("Chicken Wings", 1)
print("Cart state:", cart)

remove_from_cart("Gulab Jamun")
print("Cart state:", cart)

print("\n========== Order Summary ==========")
subtotal = 0
for c in cart:
    item_n = c["item"]
    q = c["quantity"]
    p = c["price"]
    row_tot = p * q
    subtotal = subtotal + row_tot
    
    name_pad = item_n.ljust(18, " ")
    print(f"{name_pad} x{q}    ₹{row_tot}")

print("------------------------------------")
gst = subtotal * 0.05

# rounding to make it look clean
subtotal_rnd = round(subtotal, 2)
gst_rnd = round(gst, 2)
total_pay = subtotal + gst
total_pay_rnd = round(total_pay, 2)

sub_pad = "Subtotal:".ljust(24, " ")
print(f"{sub_pad} ₹{subtotal_rnd}")

gst_pad = "GST (5%):".ljust(24, " ")
print(f"{gst_pad} ₹{gst_rnd}")

pay_pad = "Total Payable:".ljust(24, " ")
print(f"{pay_pad} ₹{total_pay_rnd}")
print("====================================")


# ======================================================================
# Task 3 - Inventory Tracker with Deep Copy
# ======================================================================
print("\n\nTask 3: Inventory Tracker with Deep Copy\n")

inventory_backup = copy.deepcopy(inventory)

# change one stock manually to show it works
print("Testing deep copy...")
inventory["Paneer Tikka"]["stock"] = 999
print("Original Inventory Paneer Tikka stock:", inventory["Paneer Tikka"]["stock"])
print("Backup Inventory Paneer Tikka stock:", inventory_backup["Paneer Tikka"]["stock"])

# restoring original state before continuing logic
inventory = copy.deepcopy(inventory_backup)
print("Restored original inventory.")

# performing deductions from final cart
print("\nFulfilling Order:")
for c in cart:
    name_it = c["item"]
    qty_req = c["quantity"]
    
    current_stock = inventory[name_it]["stock"]
    if qty_req > current_stock:
        print(f"Warning: Insufficient stock for {name_it}. Deducting only {current_stock}.")
        inventory[name_it]["stock"] = 0
    else:
        inventory[name_it]["stock"] = current_stock - qty_req

# checking reorder alerts loop
print()
for it_name in inventory:
    stk = inventory[it_name]["stock"]
    lvl = inventory[it_name]["reorder_level"]
    
    if stk <= lvl:
        print(f"⚠ Reorder Alert: {it_name} - Only {stk} unit(s) left (reorder level: {lvl})")

print("\nVerifying Backup vs Inventory at the end:")
print("Inventory Paneer Tikka stock:", inventory["Paneer Tikka"]["stock"])
print("Backup Paneer Tikka stock:", inventory_backup["Paneer Tikka"]["stock"])


# ======================================================================
# Task 4 - Daily Sales Log Analysis
# ======================================================================
print("\n\nTask 4: Daily Sales Log Analysis\n")

# 1. Total revenue per day
print("Revenue per day:")
best_day_date = ""
highest_rev = 0

for d in sales_log:
    daily_tot = 0
    orders_list = sales_log[d]
    for o in orders_list:
        daily_tot = daily_tot + o["total"]
        
    print(f"{d}: ₹{daily_tot}")
    
    if daily_tot > highest_rev:
        highest_rev = daily_tot
        best_day_date = d

print(f"\nBest-selling day: {best_day_date} (₹{highest_rev})")

# 2. Most ordered item across all days
item_counts = {}
for d in sales_log:
    orders_list = sales_log[d]
    for o in orders_list:
        items_in_order = o["items"]
        for itm in items_in_order:
            if itm not in item_counts:
                item_counts[itm] = 1
            else:
                item_counts[itm] = item_counts[itm] + 1

max_orders = 0
top_item = ""
for itm in item_counts:
    if item_counts[itm] > max_orders:
        max_orders = item_counts[itm]
        top_item = itm

print(f"\nMost ordered item: {top_item} (ordered {max_orders} times)")

# 3. Add new day
print("\n--- Updating sales log with new day ---")
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# recalculating
print("\nUpdated Revenue per day:")
best_day_date_new = ""
highest_rev_new = 0

for d in sales_log:
    daily_tot = 0
    orders_list = sales_log[d]
    for o in orders_list:
        daily_tot = daily_tot + o["total"]
        
    print(f"{d}: ₹{daily_tot}")
    
    if daily_tot > highest_rev_new:
        highest_rev_new = daily_tot
        best_day_date_new = d

print(f"\nUpdated Best-selling day: {best_day_date_new} (₹{highest_rev_new})")

# 4. Enumerated list
print("\nAll Orders List:")
flat_orders = []
for d in sales_log:
    for o in sales_log[d]:
        val = {"date": d, "order_info": o}
        flat_orders.append(val)

# using enumerate specifically as requested
for idx, order_data in enumerate(flat_orders, start=1):
    d = order_data["date"]
    o = order_data["order_info"]
    oid = o["order_id"]
    tot = o["total"]
    
    # manually joining instead of .join to look slightly less robotic
    items_combined = ""
    for i in range(len(o["items"])):
        items_combined += o["items"][i]
        if i < len(o["items"]) - 1:
            items_combined += ", "
            
    print(f"{idx}.  [{d}] Order #{oid}  - ₹{tot} - Items: {items_combined}")
