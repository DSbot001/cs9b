# Lecture 2: class
# August 4th



#Dictionary 
student = {"name": "Alice", "score": 92}

student["name"]          # "Alice"
student["age"] = 20      # adds a new key
del student["age"]       # removes a key

for key in student:
    print(key, student[key])

for key, value in student.items():   # more common pattern
    print(key, value)

"name" in student         # True — checks keys, not values





#Class
class Golfer:
    def __init__(self, name,scores = None):
        self.name = name
        self.scores = []
        self.scores = [] if scores is None else scores


    def add_round(self, score):
        self.scores.append(score)

    def average_score(self):
        return sum(self.scores) / len(self.scores)

dylan = Golfer("Dylan")

dylan.add_round(70)
dylan.add_round(72)
dylan.add_round(68) # what is executed: Golfer.add_round(dylan, 70)

print(dylan.average_score())

mason = Golfer("Mason",[69,66,72,62,76])
print(mason.average_score())


class BasketballPlayer:

    # Initialize a new BasketballPlayer object
    def __init__(self, name):
        # Store the player's name as an attribute
        self.name = name
        # Create an empty list for the player's game scores
        self.points_arr = []

    # Add one game's points to the player's record
    def add_game(self, points):
        # Append the points to the end of the list
        self.points_arr.append(points)

    # Calculate and return the player's average points
    def average_points(self):
        # Check whether the player has played any games
        if len(self.points_arr) > 0:
            # Divide total points by number of games
            return sum(self.points_arr) / len(self.points_arr)
        else:
            return 0

    # Define how the object appears when printed
    def __str__(self):
        game_count = len(self.points_arr)
        # Call average_points() and store the returned result
        average = self.average_points()
        # Return a readable description of the player
        return f"{self.name} has played {game_count} games and averages {average} points per game."

    # Define safe equality comparison
    def __eq__(self, other):
        # Check whether other is a BasketballPlayer object
        if isinstance(other, BasketballPlayer):
            # Compare their attributes if the types are appropriate
            return self.name == other.name and self.points_arr == other.points_arr
        # Return False when other is a different type
        return False


# Create a BasketballPlayer object
shai = BasketballPlayer("Shai Gilgeous-Alexander")

# Add three games to shai's record
shai.add_game(32)
shai.add_game(28)
shai.add_game(36)

# Python automatically calls shai.__str__()
print(shai) # BasketballPlayer.__str__()
#output: Shai Gilgeous-Alexander has played 3 games and averages 32.0 points per game. 



##__eq__
# Create the first object
player1 = BasketballPlayer("Shai")

# Create a second, separate object
player2 = BasketballPlayer("Shai")


# Both objects contain the same name
print(player1.name)  # Shai
print(player2.name)  # Shai


# __eq__ compares their attributes
print(player1 == player2)  # True

# is still checks whether they are literally the same object
print(player1 is player2)  # False



##ALIASES
# Create the first object
player1 = BasketballPlayer("Shai")

# Create a completely separate second object
player2 = BasketballPlayer("Shai")

# They contain equal information
print(player1 == player2)  # True

# But they are NOT the same object
print(player1 is player2)  # False

# Change only player2
player2.add_game(35)

# player1 is unaffected
print(player1.points_arr)  # []

# player2 contains the new score
print(player2.points_arr)  # [35]