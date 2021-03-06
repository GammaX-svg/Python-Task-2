class Flower:
    def __init__(self, name='Flower_1', no_of_petals=1,price=1.0):
        self.name = name
        self.no_of_petals = no_of_petals
        self.price = price
    def __repr__(self):
        return 'Flower->{}, {} petals, {} NGN'.format(self.name, self.no_of_petals, self.price)
    def set_name(self, new_name):
        self.name = new_name
    def set_no_of_petals(self, no):
        self.no_of_petals = no
    def set_price(self, new_price):
        self.price = new_price
    def get_name(self):
        return self.name
    def get_no_of_petals(self):
        return self.no_of_petals
    def get_price(self):
        return self.price
if __name__ == '__main__':
    my_flower = Flower('Hibiscus',3,20)
    my_flower.set_price(2000)
    print(my_flower)