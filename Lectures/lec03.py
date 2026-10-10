from lec02 import Golfer
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
assert square(5) == 26 #AssertionError
