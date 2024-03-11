# almost everything in python is an object, with its properties & methods
# to create a class, use class keyword. A class is a blueprint for creating objects

# All classes have a function called __init__(), which is always executed when the class is being initiated. Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

# base class
class Vehicle:

    def __init__(self, make, model):  # parameters
        self.make = make
        self.model = model
    # 2 methods - moves, get make model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


# instances of the Vehicle class
my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
# this prints out Im a Tesla Model 3, moves along
my_car.get_make_model()
my_car.moves()

# create a new object from the vehicle class
your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


# create subclasses that inherit the Vehicle class
# airplane has more info than parent class, so add initializer to pass in more information
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')
# check snapchat ai on explanation


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')
# def moves(self): ovverrides the moves method from the Vehicle class class


class GolfCart(Vehicle):
    pass
# pass merely just passes through the default implementation from the Vehicle class


# create instacnes of subclasses
cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')


cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


# polymorphism
# this basically replicates the entire program and adds 2 line spaces to seperate them
print('\n\n')


for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
