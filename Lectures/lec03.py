# from [filename without .py] import [class name/conponent]
from lec02 import Student 
import copy


## Deep and Shallow Copy

# Create a nested list
a = [[1, 2], [3, 4]]


# 1. No copy: aliasing
# b points to the exact same object as a
b = a
# Modify an inner list
b[0].append(100)
#print(a) : [[1, 2, 100], [3, 4]]
a is b  # True


# 2. Shallow copy
# Create a nested list
a = [[1, 2], [3, 4]]
# Create a SHALLOW copy
b = a.copy()
print(a is b)  # False
print(a[0] is b[0])  # True
#The inner lists were NOT copied.
b.append([5, 6])

print(a)  # [[1, 2], [3, 4]]
print(b)  # [[1, 2], [3, 4], [5, 6]]

# 3. Deep Copy
# Import Python's copy module
# Create the original nested list
a = [[1, 2], [3, 4]]
# Create a completely independent deep copy
b = copy.deepcopy(a)

# Outer lists are different objects
print(a is b)  # False
# Inner lists are ALSO different objects
print(a[0] is b[0])  # False

# Modify b's inner list
b[0].append(100)
# a is unaffected
print(a)  # [[1, 2], [3, 4]]

# Only b changes
print(b)  # [[1, 2, 100], [3, 4]]






## Errors
# print("Hello")      # Runs normally
# print(5 / 0)        # Error happens here → program stops
# print("Goodbye")    # Never runs


# 10 / 0
# produces:
# ZeroDivisionError

# Another example:
# numbers = [10, 20, 30]
# print(numbers[5])
# produces: IndexError. Because index 5 doesn't exist.

# And:
# x = int("Dylan")
# produces:ValueError


## try & exceptions
try:
    x = 10 / 0  # Try doing this
except ZeroDivisionError:
    print("You cannot divide by zero!") # If something goes wrong, do this instead


# try:
#     numbers = [10, 20, 30]
#     print(numbers[5])          # IndexError happens

# except ZeroDivisionError:     # ❌ Does NOT catch IndexError
#     print("Something went wrong")

# print("Done")                 # ❌ Never reached


#This is why we want multiple exceptions
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except ZeroDivisionError:
    print("You cannot divide by zero!")

except IndexError:
    print("That index does not exist!")

except ValueError:
    print("Invalid value!")


## Raise

def set_age(age):
    # Check if the age is invalid
    if age < 0:

        # Manually create a ValueError
        raise ValueError("Age cannot be negative")

    # Only reached if no exception occurred
    print(f"Age is {age}")


try:
    set_age(-5)

except ValueError as e:
    print(e)

print("Program continues")

#The flow is:
# set_age(-5)
#       ↓
# raise ValueError(...)
#       ↓
# leave set_age() immediately
#       ↓
# except ValueError catches it
#       ↓
# program continues



## Testing
def square(x):
    return x * x


assert square(2) == 4
#assert square(5) == 26 #AssertionError



class Courses:
    ''' Classing representing a collection of courses.
    Courses are organized by a dictiionaary where the key is the course number and the corres
    ponding value is the a list of studrents in the course'''

    def __init__(self):
        self.courses = {}

    def add_student(self, student, courseID):
        '''Method to add a student to a course. If the course does not exist, 
        it is created. If the student is already in the course, 
        they are not added again.'''

        if self.courses.get(courseID) is None:
            self.courses[courseID] = [student]
        elif not student in self.courses.get(courseID):
            self.courses[courseID].append(student)

    def printCourses(self):
        '''Method to print all courses and their students.'''
        for courseID in self.courses:
            print(courseID, self.courses[courseID])

student1 = Student("Alice", 1112221)
student2 = Student("Bob", 1112222)
student3 = Student("Charlie", 1112223) 

UCSB = Courses()
UCSB.add_student(student1, "CS8")
UCSB.add_student(student2, "CS9")
UCSB.add_student(student3, "CS24")
UCSB.add_student(student1, "CS24") # Alice is also in CS24
UCSB.add_student(student2, "CS24") # Bob is also in CS24

UCSB.printCourses()