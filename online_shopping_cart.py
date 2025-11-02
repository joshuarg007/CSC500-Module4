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

# Step 1: Define ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

# Step 2: Prompt the user for two items
print("Item 1")
item1_name = input("Enter the item name:\n")
item1_price = float(input("Enter the item price:\n"))
item1_quantity = int(input("Enter the item quantity:\n"))
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

print("\nItem 2")
item2_name = input("Enter the item name:\n")
item2_price = float(input("Enter the item price:\n"))
item2_quantity = int(input("Enter the item quantity:\n"))
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

# Step 3: Output the total cost
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost:.0f}")
