from tabulate import tabulate

class Shoes:
    def read_file():
        try:
            file = open("inventory.txt","r")
            shoes = file.readlines()
            print(shoes)
        except FileNotFoundError:
            print("This file does not exist in Python")
        finally:
            file.close()

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

sku95000 = Shoes("Vietnam","SKU95000","Air Mag",2000,2)
sku20394 = Shoes("France","SKU20394","Eric Koston 1",2322,17)
sku44386 = Shoes("South Africa","SKU44386","Air Max 90",2300,20)
sku29077 = Shoes("United States","SKU29077","Cortez",970,60)
sku57443 = Shoes("Australia","SKU57443","Waffle Racer",2700,4)

def code():
    shoe = input("Enter the shoe's code: ")
    if shoe =="sku95000":
        print(f"The code is for: {sku95000.product}")
    elif shoe =="sku20394":
        print(f"The code is for: {sku20394.product}")
    elif shoe =="sku44386":
        print(f"The code is for: {sku44386.product}")
    elif shoe =="sku29077":
        print(f"The code is for: {sku29077.product}")
    elif shoe =="sku57443":
        print(f"The code is for: {sku57443.product}")
    else:
        print("We dont have the code/shoe in our system")

code()

shoe_list = [sku95000.quantity, sku20394.quantity, sku44386.quantity, sku29077.quantity, sku57443.quantity]
shoe_list.sort()
print(f"The Waffle racer shoe has a low quantity of {shoe_list[0]} and needs to be restocked")
print(f"The Cortez shoe has a high quantity of {shoe_list[4]} and is now marked to be on SALE")

def value_per_item():
    
    shoe1 = sku95000.quantity * sku95000.cost
    print(f"The value for this shoe is {shoe1}")
    shoe2 = sku20394.quantity * sku20394.cost
    print(f"The value for this shoe is {shoe2}")
    shoe3 = sku44386.quantity * sku44386.cost
    print(f"The value for this shoe is {shoe3}")
    shoe4 = sku29077.quantity * sku29077.cost
    print(f"The value for this shoe is {shoe4}")
    shoe5 = sku57443.quantity * sku57443.cost
    print(f"The value for this shoe is {shoe5}")

    product1 = "Vietnam","SKU95000","Air Mag",2000,2,shoe1
    product2 = "France","SKU20394","Eric Koston 1",2322,17,shoe2
    product3 = "South Africa","SKU44386","Air Max 90",2300,20,shoe3
    product4 ="United States","SKU29077","Cortez",970,60,shoe4
    product5 = "Australia","SKU57443","Waffle Racer",2700,4,shoe5

    product =       [["Vietnam","SKU95000","Air Mag",2000,2,shoe1],
                    ["France","SKU20394","Eric Koston 1",2322,17,shoe2],
                    ["South Africa","SKU44386","Air Max 90",2300,20,shoe3],
                    ["United States","SKU29077","Cortez",970,60,shoe4],
                    ["Australia","SKU57443","Waffle Racer",2700,4,shoe5]]

    print(tabulate(product, headers = ["country", "code", "product", "cost", "quantity","value"]))

value_per_item()

