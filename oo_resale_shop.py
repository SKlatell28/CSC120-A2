from computer import *


class ResaleShop:
    
    inventory: list

    #Constructor (makes the inventory/list)
    def __init__(self):
        self.inventory = []

    #Buys a new computer for the shop and adds it to the inventory
    def buy(self, C: Computer):
        
        print("")
        print(f"Just bought a {C.description} for ${C.price}!")
        print("")
        #####
        self.inventory.append(C)
    
    #Prints out everything currently in the stores inventory
    def print_inventory(self):
        pass
        print("")
        print("Checking Inventory :)")
        if self.inventory:
            for i in self.inventory:
                print(f"You have a {i.description}, with processor_type: {i.processor_type}")
        else: 
            print("You actually do NOT own any computers at all right now:)")
        print("")
    
    #Sells the computers in the inventory
    def sell(self, C: Computer):
        if C in self.inventory:
            print("")
            print(f"Now selling your {C.description} for ${C.price}!")
            self.inventory.remove(C)
            print("")


    #Refurbishes a computer and updates it's price
    def refurbish(self, C: Computer):
        if C in self.inventory:
            print("")
            print(f"Refurbishing your {C.description} made in {C.year_made}")
            if (C.year_made < 2000):
                print("This computer is really too old to sell, consider donating it instead...")
                C.price = 0
            elif (C.year_made < 2012):
                print("We can upgrade this a little...I guess...")
                print(f"Upgrading the operating system from {C.operating_system}", end=" ")
                C.operating_system = "macOS Montery"
                print(f"to {C.operating_system}")
                C.price += 250
            elif (C.year_made < 2018):
                print("We can upgrade this to a newer model!")
                print(f"Upgrading the operating system from {C.operating_system}", end=" ")
                C.operating_system = "macOS Montery"
                print(f"to {C.operating_system}")
                C.price += 550
            else:
                print("Wow! This model is almost new! Still, we can upgrade this to a newer model!")
                print(f"Upgrading the operating system from {C.operating_system}", end=" ")
                C.operating_system = "macOS Montery"
                print(f"to {C.operating_system}")
                C.price += 1000
            print(f"The price of your product is now ${C.price}")
            print("")


def main():
    d = ResaleShop()
    name: Computer = Computer ("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5",
                                 1024, 64, "macOS Big Sur", 2013, 1500)
    d.buy(name)
    d.print_inventory()
    d.refurbish(name)
    d.sell(name)
    d.print_inventory()


if __name__ == "__main__":
    main()

