from menu import menu, clear, header
from item import Item
import datetime
import pickle

catalog = []
log = []
last_id = 0
data_file = "warehouse.data"
log_file = "log.data"


def save_catalog():
    global data_file
    # Create file (overwrite), open it to Write Binary "wb".
    writer = open(data_file, "wb")
    pickle.dump(catalog, writer)
    writer.close()
    print("** Data Saved")


def read_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file, "rb")
        temporal_list = pickle.load(reader)

        for item in temporal_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id

        how_many = len(catalog)
        print("** Loaded" + str(how_many) + "items")

    except:
        print("** No data file found")


def save_log():
    global log_file
    writer = open(log_file, "wb")
    pickle.dump(log, writer)
    writer.close()
    print("** Log Saved")


def read_log():
    try:
        global log_file
        reader = open(log_file, "rb")
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)

        how_many = len(log)
        print("** Loaded" + str(how_many) + "Entry Log")
    except:
        print("** Error loading Log Entry")


def register_item():
    global last_id
    header("Register new item")

    title = input("New item name: ")
    category = input("Item's category: ")
    price = float(input("Price of item: "))
    inventory = int(input("Amount of items: "))

    new_item = Item()
    last_id += 1
    new_item.id = last_id
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.inventory = inventory

    catalog.append(new_item)
    add_log_event("New Item", "Added Item: ", + str(last_id))
    print("Item has been created...")


def display_catalog():
    size = len(catalog)
    header("Current Catalog(" + str(size) + "items")

    print("|" + "ID".rjust(2)
          + " | " + "Title".ljust(20)
          + " | " + "Category".ljust(15)
          + " | " + "Price".rjust(10)
          + " | " + "inventory".rjust(5) + "|")
    print("-" * 70)

    for item in catalog:
        print("|" + str(item.id).rjust(2)
              + " | " + item.title.ljust(20)
              + " | " + item.category.ljust(15)
              + " | " + str(item.price).rjust(10)
              + " | " + str(item.inventory).rjust(5) + "|")
    print("-" * 70)


def out_of_inventory():
    size = len(catalog)
    header("Current Catalog(" + str(size) + "items")

    print("|" + "ID".rjust(2)
          + " | " + "Title".ljust(20)
          + " | " + "Category".ljust(15)
          + " | " + "Price".rjust(10)
          + " | " + "inventory".rjust(5) + "|")
    print("-" * 70)

    for item in catalog:
        if(Item.inventory == 0):
            print("|" + str(item.id).rjust(2)
                  + " | " + item.title.ljust(20)
                  + " | " + item.category.ljust(15)
                  + " | " + str(item.price).rjust(10)
                  + " | " + str(item.inventory).rjust(5) + "|")
    print("-" * 70)


def update_inventory(option):
    display_catalog()
    id = int(input("Select ID from list: "))

    found = False

    for item in catalog:
        if(item.id == id):
            found = True

            if(option == 1):
                inventory = int(input("New inventory value: "))
                item.inventory = inventory
                print("Inventory has been updated")
                add_log_event("SetInventory", "Updated stock for item: " + str(item.id))

            else:
                sold = int(input("Number of items to sell: "))
                item.inventory -= sold
            print("Sale registered")
            add_log_event("Sale", "Sold " + str(sold) + "Number of item: " + str(item.id))


    if(not found):
        print("Error: ID not found")


def inventory_total():
    total = 0.0
    for item in catalog:
        total += (item.price * item.inventory)
    print("Total value of inventory = $" + str(total))


def remove_item():
    display_catalog()
    id = int(input("Select ID of the item to remove: "))
    for item in catalog:
        if(item.id == id):
            catalog.remove(item)
            found = True
            add_log_event("Remove", "Removed item: " + str(item.id))
            break

    if(found):
        print("Item removed from catalog")
    else:
        print("Error: invalid entry")

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%b/%d/%Y/%T")

def add_log_event(event_type, event_description):
    entry = get_current_time() + " | " + event_type.ljust(10) + " | " + event_description
    log.append(entry)
    save_log()

def print_log():
    header("Logged Events")
    for entry in log:
        print(entry)

read_catalog()
read_log()
input("Press Enter to continue")

option = ""
while(option != 'x'):
    clear()
    menu()
    option = input("Please select an option: ")

    if(option == "1"):
        register_item()
        save_catalog()
    elif(option == "2"):
        display_catalog()
    elif(option == "3"):
        out_of_inventory()
    elif(option == "4"):
        update_inventory(1)
        save_catalog()
    elif(option == "5"):
        inventory_total()
    elif(option == "6"):
        remove_item()
        save_catalog()
    elif(option == "7"):
        update_inventory(2)
        save_catalog()
    elif(option == "8"):
        print(log)

    input("Press 'Enter' to continue")
