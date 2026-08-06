class Animal:
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
    def __init__(self, species, name, sound):
        # Let Animal initialize the inherited attributes
        super().__init__(species, name)

        # Cow initializes its own extra attribute
        self.sound = sound

    def getSound(self):
        parent_sound = super().getSound()  #calls the parent.getSound()
        return parent_sound + " Moo!"





cow = Cow("Cow", "Betsy", "Moo") # Passes in data for Animal AND Cow
unicorn = Animal("Unicorn", "Lala")

zoo = [cow, unicorn]
print(cow.getSound())
print(cow.species)  # Cow
print(cow.name)     # Betsy
print(cow.sound)    # Moo

for i in zoo:
	print(i.getAttributes())
	print(i.getSound())
	print("---")





class A(Exception):
	pass

class B(A): # B inherits from A (B IS-A A type, since A is a Exception type, B is also)   
	pass

class C(Exception):
	pass

try:
	x = int(input("Enter a positive number: "))
	if x < 0:
		raise B() # Change this to A() and C() and observe...
except C:
	print("Exception of type C caught")  
except A:
	print("Exception of type A caught") #stops at the first one
except B:
	print("Exception of type B caught") # Will never get called
except Exception:
	print("Exception of type Exception caught")

print("Resuming execution")