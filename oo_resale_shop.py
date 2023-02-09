from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []
    itemID = 0 
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        pass # You'll remove this when you fill out your constructor


    # What methods will you need?
    def buy(inventory, computer):
        itemID += 1 # increment itemID
        inventory[itemID] = computer
        return itemID

    def sell(item_id, inventory):
        if item_id in inventory:
            del inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def update_price(self, new_price):
        self.price = new_price

    def update_version(self, new_version):
        self.version = new_version

    def refurbish(self, new_os):
         if int(computer.year_made) < 2000:
            Computer[self.price] = 0 # too old to sell, donation only
         elif int(self.year_made) < 2012:
            Computer[self.year_made] = 250 # heavily-discounted price on machines 10+ years old
         elif int(self.year_made) < 2018:
            Computer[self.price] = 550 # discounted price on machines 4-to-10 year old machines
         else:
            Computer[self.price] = 1000 # recent stuff
         if new_os is not None:
            Computer[self.operating_system] = new_os # update details after installing new OS

    def add_computer(self, computer):
        self.inventory.append(computer)
        # 1. call computer(...)constructor 
        #    to create a new Computer instance
        # 2. call inventory.append(...) to add the 
        #    new Computer instance to the inventory


    def print_inventory():
        if store.inventory:
            for computer in store.inventory:
                print("Description: " + computer.description)
                print("Processor Type: " + computer.processor_type)
                print("Storage: " + str(computer.hard_drive_capacity))
                print("Memory: " + str(computer.memory))
                print("Operating System: " + computer.operating_system)
                print("Year Made: " + str(computer.year_made))
                print("Price: $" + str(computer.price))
        else:
            print("No results to display for inventory! Come back later")
 
    
computer = Computer("Macbook Pro", "M2 Chip", 512, 16, "MacOS", 2022, 1200)

store = ResaleShop()

store.add_computer(computer)

store.refurbish(computer)




    