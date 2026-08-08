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

class LinkedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def addToFront(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

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