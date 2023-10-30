import csv
with open('sample_data.csv', mode = 'r') as file:
    csv_file = csv.reader(file)
    for lines in csv_file:
        print(lines)
class Item:

    def __init__(self, name, category, perishable, stock, sell_price):
        #initialise attributes
        self.name = name
        self.category = category
        self.perishable = perishable
        self.stock = stock
        self.sell_price = sell_price

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_perishable(self):
        return self.perishable

    def get_stock(self):
        return self.stock

    def get_sell_price(self):
        return self.sell_price

    def __str__(self):
        return f'Item: {self.name}, {self.category}, {self.perishable}, {self.stock}, {self.sell_price}'

    def __repr__(self):
        return f'Item: {self.name}, {self.category}, {self.perishable}, {self.stock}, {self.sell_price}'

    def __eq__(self, other):
        if isinstance(other, Item): #checks if other is same data type as Item
            if self.name == other.name: #checks if two items are equal to each other through the name
                return True
        return False

    def __hash__(self):
        return hash((self.name, self.category, self.perishable, self.stock, self.sell_price))
