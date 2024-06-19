#Inventory Management System for a Grocery Store by File Handling and Exception Handling.

import datetime as dt
#Created a class Products:
class Products:
    def __init__(self, Name, Category, Price, Quantity, ExpiryDate):
        self.Name = Name
        self.Category = Category
        self.Price = Price
        self.Quantity = Quantity
        self.ExpiryDate = ExpiryDate
    
#Function is defined/created to check the expiry date of products in inventory
    def Expired(self):
        today = dt.date.today()
        return self.ExpiryDate < today
    
    def __str__(self):
        return f"{self.Name}, {self.Category}, {self.Price}, {self.Quantity}, {self.ExpiryDate}"

# Initialized/created an empty list for inventory.
Inventory = []

# Function is defined/created to add a product to the inventory.
def Add_Product_to_Inventory(prdt):
    Inventory.append(prdt)

# Function is defined/created to remove a product from the inventory by the name.
def Remove_Product_from_Inventory(ProductName):
    global Inventory
    Inventory = [prdt for prdt in Inventory if prdt.Name != ProductName]

# Function is defined/created to search for products their by name or category.
def Search_Products(SearchProduct):
    return [prdt for prdt in Inventory if SearchProduct.lower() in prdt.Name.lower() or SearchProduct.lower() in prdt.Category.lower()]

# Function is defined/created to list all the products in the inventory.
def List_all_Products():
    for prdt in Inventory:
        print(prdt)

# Function is defined/created to categorize products by category.
def Categorize_Products():
    Categories = {}
    for prdt in Inventory:
        if prdt.Category not in Categories:
            Categories[prdt.Category] = []
        Categories[prdt.Category].append(prdt)
    return Categories

# Function is defined/created to remove the expired products from the inventory.
def RemoveExpiredProducts():
    global Inventory
    today = dt.date.today()
    Inventory = [prdt for prdt in Inventory if not prdt.Expired()]

# Function is is defined/created to save inventory to a file.
def SaveInventory(filename):
    try:
        file = open('C:\\Users\\Lenovo\\Desktop\\Python\\filename','a+')
        with open(filename, 'w') as file:
            for product in Inventory:
                file.write(f"{product}\n")
        print(f"Inventory saved to {filename}")
    except IOError:
        print(f"Error: Could not write to file {filename}")

# Function is defined/created to load the inventory from a file.
def LoadInventory(filename):
    global Inventory
    try:
        with open(filename, 'r') as file:
            Inventory = []
            for line in file:
                data = line.strip().split(', ')
                Name = data[0]
                Category = data[1]
                Price = float(data[2])
                Quantity = int(data[3])
                ExpiryDate = dt.date.fromisoformat(data[4])
                Product = Products(Name, Category, Price, Quantity, ExpiryDate)
                Inventory.append(Product)
        print(f"Inventory loaded from {filename}")
    except IOError:
        print(f"Error: Could not read from file {filename}")

# Input data or the product detals of the inventory.
prdtdata = [
    ("Mango", "Fruits", 50.00, 60, dt.date(2024, 7, 1)),
    ("Apple", "Fruits", 30.00, 50, dt.date(2024, 7, 7)),
    ("Orange", "Fruits", 20.00, 40, dt.date(2024, 6, 20)),
    ("Watermelon", "Fruits", 50.00, 30, dt.date(2024, 6, 30)),
    ("Cabbage", "Vegetables", 20.00, 25, dt.date(2024, 6, 25)),
    ("Brinjal", "Vegetables", 15.00, 20, dt.date(2024, 6, 22)),
    ("Cauliflower", "Vegetables", 25.00, 25, dt.date(2024, 6, 24)),
    ("Milk", "Dairy Products", 46.00, 48, dt.date(2024, 6, 16)),
    ("Paneer", "Dairy Products", 75.00, 20, dt.date(2024, 7, 20)),
    ("Cheese", "Dairy Products", 70.00, 46, dt.date(2024, 7, 20))
]

#Check the inputs in Inventory 
for inputs in prdtdata:
    prdt = Products(*inputs)
    Add_Product_to_Inventory(prdt)

# Save initial inventory to a file
SaveInventory("Inventory.txt")

# List all the products in inventory before removing the expired products from inventory.
print("\nList of products before removing the Expired Products from Inventory:")
List_all_Products()

#Search the products in the inventory.
print("\nSearching for 'Mango':", [prdt.Name for prdt in Search_Products("Mango")])
print("Searching for 'Apple':", [prdt.Name for prdt in Search_Products("Apple")])
print("Searching for 'Orange':", [prdt.Name for prdt in Search_Products("Orange")])
print("Searching for 'Watermelon':", [prdt.Name for prdt in Search_Products("Watermelon")])
print("Searching for 'Cabbage':", [prdt.Name for prdt in Search_Products("Cabbage")])
print("Searching for 'Brinjal':", [prdt.Name for prdt in Search_Products("Brinjal")])
print("Searching for 'Cauliflower':", [prdt.Name for prdt in Search_Products("Cauliflower")])
print("Searching for 'Milk':", [prdt.Name for prdt in Search_Products("Milk")])
print("Searching for 'Paneer':", [prdt.Name for prdt in Search_Products("Paneer")])
print("Searching for 'Cheese':", [prdt.Name for prdt in Search_Products("Cheese")])

# Removing the expired products from the inventory.
RemoveExpiredProducts()

# List all the products in inventory after removing the expired products from inventory.
print("\nList of products after removing the Expired Products from the Inventory:")
List_all_Products()

# To Save the updated inventory into a file.
SaveInventory("UpdatedInventory.txt")

# To Load the inventory from file
LoadInventory("Inventory.txt")
print("\nAfter Loading Inventory from a file:")
List_all_Products()