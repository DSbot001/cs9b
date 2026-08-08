'''Recursion, Python Lists vs. Dictionaries '''


def factorial(n):
	if n == 0:      # base case
		return 1
	return n * factorial(n-1)


def fibonnaci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonnaci(n-1)+ fibonnaci(n-2)


def sum_list(nums):
    if len(nums) == 0:
        return 0

    return num[0] + sum_list(nums[1:])


    
print (fibonnaci(4))



def mystery(n):
    if n == 0:
        return

    print(n)
    mystery(n - 1)
    print(n)

mystery(3)  # 3 2 1 1 2 3 



'''Python Lists vs. Python Dictionaries'''


# Set up our data structures
DICT = {} #create an empty dictionary 
infile = open("wordlist.txt", 'r')
for x in infile: # x goes through each line in the file
	DICT[x.strip()] = 0 # x.strip() <- removes whitespace/newlines from both ends. and assign each line with value 0.  ex: "apple\n" becomes "apple":0
print(len(DICT))
infile.close() # close the file after we’re done with it.

WORDLIST = []
for y in DICT: # put the DICT keys into WORDLIST
	WORDLIST.append(y)
print(len(WORDLIST))


# Algorithm 1 - Lists
from time import time
start = time()
infile = open("PeterPan.txt", 'r', encoding="utf-8")
largeText = infile.read()    #.read() reads the entire file into one sting 
infile.close()
counter = 0
words = largeText.split() #.split() breaks a string into pieces using whitespace.
for x in words:
	x = x.strip("\"\'()[]{},.?<>:;-").lower()
	if x in WORDLIST:
		counter += 1
end = time()
print("Using Python list algorithm we found", counter)
print("Time elapsed with WORDLIST (in seconds):", end - start)   


# Algorithm 2 - Dictionaries
start = time()
infile = open("PeterPan.txt", 'r', encoding="utf-8")
largeText = infile.read()
infile.close()
words = largeText.split()
counter = 0
for x in words:
	x = x.strip("\"\'()[]{},.?<>:;-").lower()
	if x in DICT: # Searching through the DICT
		counter += 1
end = time()
print("Using Python DICT algorithm we found", counter)
print("Time elapsed with DICT (in seconds):", end - start)      


# List:
# "banana" → search one-by-one → O(n)

# Dictionary:
# "banana" → hash function → location → check there → average O(1)