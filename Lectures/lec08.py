'''Lecture 9
Stacks, Queues, Deques'''






'''LIFO - Last In, First Out'''

# A Stack follows the LIFO principle:
# The LAST item added is the FIRST item removed.
#
# Think of a stack of plates:
# You add plates to the top and remove plates from the top.

# Example:
# push 10 -> [10]
# push 20 -> [10, 20]
# push 30 -> [10, 20, 30]
# pop()  -> removes 30
# Result -> [10, 20]

# Main Stack operations:
# push(item) -> add item to the top    O(1)
# pop()      -> remove and return the top item O(1)
# peek()     -> view the top item without removing it O(1)

# pytests
def test_insertIntoStack():
	s = Stack()
	s.push("Hi")
	s.push("There")
	
	assert s.size() == 2
	assert s.peek() == "There"
	assert s.isEmpty() == False

def test_deleteFromStack():
	s = Stack()
	s.push("There")
	s.push("Hi")
	x = s.pop()
	assert x == "Hi"
	assert s.peek() == "There"
	assert s.size() == 1
	assert s.isEmpty() == False
	y = s.pop()
	assert y == "There"
	assert s.size() == 0
	assert s.isEmpty() == True



class Stack:
	def __init__(self):  # initialize an empty list to store stack items
		self.items = []

	def isEmpty(self):        #returns a boolean value to check if the stack is empty
		return self.items == []

	def push(self, item):      #add a element in the end of the list
		self.items.append(item)

	def pop(self):  #remove and return the last appended element
		return self.items.pop()

	def peek(self):         #return top item WITHOUT removing it
		return self.items[-1]

	def size(self):           #returns the num of elemeents of the stack
		return len(self.items)


test_insertIntoStack()




'''Queue - FIFO (First In, First Out)'''

# A Queue follows the FIFO principle:
# The FIRST item added is the FIRST item removed.
#
# Think of people waiting in a line:
# The first person to enter the line is the first person to leave.

# Example:
# enqueue 10 -> [10]
# enqueue 20 -> [20, 10]
# enqueue 30 -> [30, 20, 10]
# dequeue()  -> removes 10
# Result     -> [30, 20]

# Main Queue operations:
# enqueue(item) -> add an item to the REAR of the queue
# dequeue()     -> remove and return the FRONT item
# isEmpty()     -> check if the queue is empty
# size()        -> return the number of items



# pytests
def test_insertIntoQueue():
	q = Queue()
	assert q.isEmpty() == True
	assert q.size() == 0
	q.enqueue("Customer 1")
	q.enqueue("Customer 2")
	assert q.isEmpty() == False
	assert q.size() == 2
    
def test_removeFromQueue():
	q = Queue()
	q.enqueue("Customer 1")
	q.enqueue("Customer 2")
	assert q.dequeue() == "Customer 1"
	assert q.isEmpty() == False
	assert q.size() == 1
	assert q.dequeue() == "Customer 2"
	assert q.isEmpty() == True
	assert q.size() == 0






class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):                # O(n)
		self.items.insert(0, item)

	def dequeue(self):            # O(1)
		return self.items.pop()

	def size(self):
		return len(self.items)




test_insertIntoQueue()
test_removeFromQueue()








class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)




d = Deque()

d.addRear(10)
d.addFront(20)
d.addRear(30)
d.removeFront()

print(d.removeRear())



def palindromeChecker(word):
    d = Deque()

    # Put every character into the deque
    for char in word:
        d.addRear(char)

    while d.size() > 1:
        front = d.removeFront()
        rear = d.removeRear()

        if front != rear:
            return False

    return True



def balanced(symbols):
    s = Stack()

    for char in symbols:

        if char == "(":
            s.push(char)

        elif char == ")":

            # No "(" available to match this ")"
            if s.isEmpty():
                return False

            s.pop()  # Match ")" with the latest "("

    # Every "(" should have been matched
    return s.isEmpty()



    
	

