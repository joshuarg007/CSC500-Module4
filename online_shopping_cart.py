#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: GutierrezJoshua_CSC500_CriticalThinking_Module2_Part1.py
Author: Joshua R. Gutierrez
Date: November 2, 2025
Version: 1.0
Description: A Python program that simulates an online shopping cart system.
It defines an ItemToPurchase class and calculates the total cost of two items
entered by the user.
"""

# Step 1: Define class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

# Step 2: Prompt user for n items
items = []  # List to store ItemToPurchase objects

for i in range(1, 3): # loop to receive user input
    print(f"Item {i}") # Header for prompt
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    items.append(ItemToPurchase(name, price, quantity))
    print()  

# Step 3: Output the total cost
print("TOTAL COST") # Header for output
total_cost = 0 # initialize total cost

for item in items: # Iterate over and add cost of each item added
    item.print_item_cost()
    total_cost += item.item_price * item.item_quantity

print(f"\nTotal: ${total_cost:.0f}")

