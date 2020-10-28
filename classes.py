class MixedDrink():
    alcohol_types = []
    toppings = []
    instructions = ''

    def __init__(self, name):
        self.name = name

    def add_alcohol(self, alcohol_type):
        if type(alcohol_type) != str:
            print('alcohol_type must be a string')
            return

        self.alcohol_types.append(alcohol_type)
