class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        item = (name, quantity)
        self.items.append(item)

    def remove_item(self, name, quantity):
        for item in self.items:
            if item[0] == name:
                new_quantity = item[1] - int(quantity)
                if new_quantity > 0:
                    self.items[self.items.index(item)] = (name, new_quantity)
                else:
                    self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        print(total)


cart1 = ShoppingCart()
cart1.add_item('Banana', 100)
cart1.add_item('Grapes', 100)
print(cart1.items)
cart1.remove_item('Grapes',50)
print(cart1.items)
cart1.calculate_total()




