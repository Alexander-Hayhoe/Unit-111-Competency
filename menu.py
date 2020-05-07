import os

def menu():
  print("-" * 30)
  print("Warehouse Control")
  print("-" * 30)

  print("[1] Register Items")
  print("[2] Display Catalog")
  print("[3] Out of inventory items")
  print("[4] Update inventory")
  print("[5] Inventory total")
  print("[6] Remove item from Catalog")
  print("[7] Register Sale")
  print("[8] Log")


  print("[x] Exit")

def header(title):
  clear()
  print("-" * 70)
  print(" " + title)
  print("-" * 70)

def clear():
  return os.system('cls' if os.name == 'nt' else 'clear')