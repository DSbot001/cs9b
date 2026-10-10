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







# Algorithm Analysis

import time

def f1(n):
	l = []
	for i in range(n):
		l.insert(0,i)
	return

def f2(n):
	l = []
	for i in range(n):
		l.append(i)
	return

print("starting f1")
start = time.time()
f1(200000)
end = time.time()
print("time elapsed: ", end - start, "seconds")

print("starting f2")
start = time.time()
f2(200000)
end = time.time()
print("time elapsed: ", end - start, "seconds")



"""

Algorithm analysis studies how an algorithm's runtime grows
when the input size n becomes larger.

Big-O describes the growth rate, not the exact runtime.

Main rules:
1. Ignore constant multipliers:
   O(10n) becomes O(n)

2. Keep only the fastest-growing term:
   O(n^2 + n + 5) becomes O(n^2)

3. Consecutive operations are added:
   O(n) + O(n) = O(2n) = O(n)

4. Nested operations are usually multiplied:
   O(n) * O(n) = O(n^2)
"""



# O(1): Constant time
def constant_time(numbers):
    print(numbers[0])


# O(n): Visit every element once
def linear_time(numbers):
    for number in numbers:
        print(number)


# O(n^2): Two nested loops
def quadratic_time(numbers):
    for first in numbers:
        for second in numbers:
            print(first, second)


# O(log n): Double each iteration
def logarithmic_time(n):
    i = 1

    while i < n:
        print(i)
        i *= 2


# O(n log n): n outer iterations,
# with log(n) inner iterations
def linearithmic_time(numbers):
    n = len(numbers)

    for number in numbers:
        i = 1

        while i < n:
            print(number, i)
            i *= 2


"""
Common growth rates:

O(1) < O(log n) < O(n) < O(n log n) < O(n^2)

One loop                         -> O(n) 
Two nested loops                -> O(n^2)
Repeatedly double/divide by 2    -> O(log n)
O(n) loop containing O(log n)   -> O(n log n)
"""