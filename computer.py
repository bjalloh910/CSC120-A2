class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system,year_made, price):
        self.description = description  
        self.processor_type = processor_type 
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system 
        self.year_made = year_made
        self.price = price
    # Remember: in python, all constructors have the same name (__init__)
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def update_price(self, new_price):
        self.price = new_price
    def update_version(self, new_version):
        self.version = new_version
    def refurbish(self, new_os):
         if int(self.year_made) < 2000:
            Computer[self.price] = 0 # too old to sell, donation only
         elif int(self.year_made) < 2012:
            Computer[self.year_made] = 250 # heavily-discounted price on machines 10+ years old
         elif int(self.year_made) < 2018:
            Computer[self.price] = 550 # discounted price on machines 4-to-10 year old machines
         else:
            Computer[self.price] = 1000 # recent stuff
         if new_os is not None:
            Computer[self.operating_system] = new_os # update details after installing new OS