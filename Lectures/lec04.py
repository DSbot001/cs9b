# Leceture4: Pytest, Operator Overloading, Inheritance

# from lec03 import square


# def test_square():
#     assert square(3) == 9
#     assert square(3) == 8

# Then type in terminal: python -m pytest test_lec04.py 


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __add__(self, other):
        return self.score + other.score

    def __le__(self, other): #less than or equal to 
        # Define what <= means for two Golfer objects
        return self.score <= other.score

    def __lt__(self, other): #less than 
        return self.score <= other.score

    #def __ge__(self, other):
    #def __gt__(self, other):

dylan = Golfer("Dylan", 68)
jack = Golfer("Jack", 71)

print(dylan + jack) #calls a.__add__(b)
print(dylan <= jack)





# Inheritage 

class Animal:
    '''Animal class type that contains attributes for all animals'''

    def __init__(self, species=None, name=None):
        self.species = species
        self.name = name

    def setName(self, name):
        self.name = name

    def getName (self):
        return self.name

    def setSpecies(self, species):
        self.species = species

    def getAttributes(self):
        return "Species: {}, Name: {}".format(self.species, self.name)

    def getSound(self):
        return "I'm an Animal!!!"





class Cow(Animal):
    # Available method for the Cow Class 
    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound 


cow = Cow("pig","Tom")
cow.setName("Betzy")
cow.setSpecies ("cow")
print (cow.getName())
print(cow.getAttributes())
cow.setSound("Moo") # Sets a Cow sound attribute to "Moo"
print(cow.getSound()) # I’m an Animal!!! (calls the Animal.getSound method)