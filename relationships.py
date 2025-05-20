# Remembering objects

# a class for a song

class Song:

    # class arribute
    all = []

    def __init__(self, name):
        self.name = name
        # store the entire instance inside the all attribute
        Song.all.append(self)

    # returns a printable version of the class instance
    def __repr__(self):
        return f"(Song <Name: {self.name}>)"

    # @classmethod
    # def example(cls):
    #     Song.all
    #     cls.all


wantam = Song("Wantam")
song2 = Song("Hips don`t lie")
song3 = Song("Sure thing")
print(Song.all)


class ShoppingList:

    # We are using this arribute to store all innstances
    # of the shopping list
    all = []
    items = {}
    count = 1
    # 10% of the total
    discount = 10

    {
        "1": "instance1",
        "2": "insance2"
    }

    def __init__(self, name, price, quantity):
        self.id = ShoppingList.count
        self.name = name
        self.price = price
        self.quantity = quantity
        # store the instance inside the class attribute
        ShoppingList.all.append(self)

        # store the instance in the items map
        ShoppingList.items[self.id] = self
        # increment the count
        ShoppingList.count += 1

    def __repr__(self):
        return f"<Item ID {self.id} -> (Name: {self.name}, Price: {self.price}, Quantity: {self.quantity})>"

    # this gives total for individual items
    def get_total(self, discount = 0):
        if discount > 0:
            pass
        # total for each item
        return self.price * self.quantity

    # this gives total for the entire items
    @classmethod
    def calculate_total(cls, discount = 0):
        # for
        total = 0
        for n in cls.all:
            total += n.price * n.quantity

        # apply discount of 10%
        # total -= total * 0.1

        # accounts for any discount
        if discount > 0:
            total -= total * (discount / 100)

        return total

    @classmethod
    def get_items_total(cls):
        total = 0
        for item in cls.items.values():
            total += item.price * item.quantity

        return total



item1 = ShoppingList(name="Sugar", price=140, quantity=1)
item2 = ShoppingList(quantity=2, name="Colgate", price=200)
item3 = ShoppingList("Majani Chai", 300, 1)
item4 = ShoppingList("Mouse", 500, 1)
item5 = ShoppingList("Cup", 800, 2)
item4.get_total(12)

print("Items", ShoppingList.all)
print("Total", ShoppingList.calculate_total(10))
print("Map Items", ShoppingList.items)

print("Total using map", ShoppingList.get_items_total())

# two entities (two params with one being optional)

# object relationships


# One to many -> Parent to Child(can be multiple)
class Parent:
    children = []

    def __init__(self, name):
        self.name = name
        # we will use this store instances of the child class
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Child:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Child {self.name}"

parent1 = Parent("Jane")
child1 = Child("Tabitha")
child2 = Child("Trevor")
# we can now be able to save child info to the parent class
parent1.add_child(child1)
parent1.add_child(child2)

print(parent1.children)

parent2 = Parent("John")
child3 = Child("Cheruiyot")
parent2.add_child(child3)
