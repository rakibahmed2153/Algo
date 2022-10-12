class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def __str__(self):
        return f"Product, Title: {self.title}, Quantity: {self.quantity}"

    def change_quantity(self, new_quentity):
        self.quantity = new_quentity   


class ShoppingList:
    def __init__(self, title):
        self.title = title
        self.items = []
    def __str__(self):
        return f"Shopping List, {self.title}, {len(self.quantity)}"
    
    def add(self, new_item):
        if isinstance(new_item, Product):
            self.items.append(new_item)
            print("Added")
        else:
            print("Already Added")  

    def show(self):
        print("Number of Items", {len(self.items)})

        for item in self.items:
            print(item.title, item.quantity)