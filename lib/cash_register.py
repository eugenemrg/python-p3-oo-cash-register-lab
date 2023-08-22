#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []
    
  def add_item(self, title, price, quantity = 1):
    for i in range(quantity):
      self.items.append(title)
    self.total += price * quantity
    self.transactions.append([title, price, quantity])
    
  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    if len(self.transactions) > 0:
      last_transaction = self.transactions.pop()
      self.total -= last_transaction[1] * last_transaction[2]
      for i in range (last_transaction[2]):
        self.items.pop()
      