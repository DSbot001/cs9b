# LinkedList.py
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext


if __name__ == "__main__":
	a = Node(10)
	b = Node(20)
	c = Node(30)
	a.next = b
	b.next = c
	print(a.next.data)       # 20
	print(a.next.next.data)  # 30
	print(c.next)            # None


class LinkedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def addToFront(self, item):  #takes in a data value/item and adds it to the front of the list
		temp = Node(item)        # Create a new node with the data value = item
		temp.setNext(self.head)   # Set the new node's next to the current head of the list
		self.head = temp     # Set the head of the list to the new node

	def length(self):
		temp = self.head
		count = 0
		while temp != None:
			count = count + 1
			temp = temp.getNext()
		return count

	def search(self, item):
		temp = self.head
		found = False
		while temp != None and not found:
			if temp.getData() == item:
				found = True
			else:
				temp = temp.getNext()
		return found

	def remove(self, item):
		current = self.head
		
		if current == None: # empty list, nothing to do
			return

		previous = None
		found = False
		while not found: #Find the element
			if current == None:
				return
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		# Case 1: remove 1st element
		if found == True and previous == None:
			self.head = current.getNext()
		
		# Case 2: remove not 1st element
		if found == True and previous != None:
			previous.setNext(current.getNext())

		