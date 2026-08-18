"""
CS9 Lecture 11 Notes
Ordered Linked Lists, Testing, and Tail References

Topics:
1. Testing the LinkedList and Node classes from Lecture 10
2. Ordered linked lists
3. Ordered insertion
4. Ordered searching
5. Keeping a tail reference
6. Runtime analysis
"""

from lec10 import LinkedList, Node


# ============================================================
# PART 1: TESTING NODE
# ============================================================

def test_NodeCreation():
    # Create a node containing 20
    n = Node(20)

    # The node should store 20 as its data
    assert n.getData() == 20

    # A new node is not connected to another node
    assert n.getNext() is None


def test_NodeSetData():
    n = Node(20)

    # Change the data from 20 to 200
    n.setData(200)

    assert n.getData() == 200


def test_NodeSetNext():
    n = Node(20)
    n2 = Node(10)

    # Connect n to n2
    n.setNext(n2)

    assert n.getNext() == n2
    assert n.getNext().getData() == 10


# ============================================================
# PART 2: TESTING THE UNORDERED LINKED LIST FROM LECTURE 10
# ============================================================

def test_createList():
    ll = LinkedList()

    # A new linked list begins with head pointing to None
    assert ll.isEmpty() is True


def test_addingNodesToList():
    ll = LinkedList()

    assert ll.isEmpty() is True

    # addToFront() places each new node at the beginning
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)

    # The resulting list is:
    # head -> False -> "Gaucho" -> 10 -> None

    assert ll.isEmpty() is False
    assert ll.length() == 3

    assert ll.search(10) is True
    assert ll.search("Gaucho") is True
    assert ll.search(False) is True
    assert ll.search("CS9") is False


def test_removeNodesFromList():
    ll = LinkedList()

    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    ll.addToFront("CS9")

    # Current list:
    # head -> "CS9" -> False -> "Gaucho" -> 10 -> None

    assert ll.length() == 4
    assert ll.search(10) is True

    # Remove the final node
    ll.remove(10)

    assert ll.search(10) is False
    assert ll.search("Gaucho") is True
    assert ll.search(False) is True
    assert ll.search("CS9") is True
    assert ll.length() == 3

    # Remove a middle node
    ll.remove(False)

    assert ll.search(False) is False
    assert ll.search("Gaucho") is True
    assert ll.search("CS9") is True
    assert ll.length() == 2
    assert ll.isEmpty() is False

    # Remove all remaining nodes
    ll.remove("Gaucho")
    ll.remove("CS9")

    # Remember to include assert here!
    assert ll.isEmpty() is True
    assert ll.length() == 0


# ============================================================
# PART 3: ORDERED LINKED LIST
# ============================================================

"""
An unordered linked list can store its values in any order:

    head -> 30 -> 10 -> 20 -> None

An ordered linked list automatically puts each new item in its
correct position:

    head -> 10 -> 20 -> 30 -> None

Because the list must remain ordered, we cannot always insert a
new node at the front. We must first find its correct position.
"""


class OrderedLinkedList:
    def __init__(self):
        # head refers to the first node
        self.head = None


    def isEmpty(self):
        # The list is empty when head points to None
        return self.head is None


    def length(self):
        current = self.head
        count = 0

        # Visit every node in the list
        while current is not None:
            count += 1
            current = current.getNext()

        return count


    def add(self, item):
        """
        Add an item while preserving ascending order.

        Example:

            Before:
            head -> 10 -> 20 -> 40 -> None

            Add 30:

            After:
            head -> 10 -> 20 -> 30 -> 40 -> None

        Runtime:
            Worst case: O(n)
            We may need to traverse the entire list.
        """

        current = self.head
        previous = None
        stop = False

        # Find the correct position for the new item
        while current is not None and not stop:

            # If current is larger than item, item belongs
            # immediately before current
            if current.getData() > item:
                stop = True

            else:
                # Move both traversal references forward
                previous = current
                current = current.getNext()

        # Create the new node
        newNode = Node(item)

        # CASE 1: Insert at the front
        #
        # This happens when:
        # - The list is empty, or
        # - The new item is smaller than the current head
        if previous is None:
            newNode.setNext(self.head)
            self.head = newNode

        # CASE 2: Insert in the middle or at the end
        else:
            newNode.setNext(current)
            previous.setNext(newNode)


    def search(self, item):
        """
        Search for an item in the ordered linked list.

        Because the list is ordered, searching can stop early.

        Example:

            head -> 5 -> 15 -> 25 -> 40 -> None

        Searching for 20 checks:

            5 -> 15 -> 25

        Once we reach 25, we know 20 cannot appear later because
        every later value must be greater than 25.

        Best case: O(1)
        Worst case: O(n)
        """

        current = self.head

        while current is not None:

            # Item was found
            if current.getData() == item:
                return True

            # We have passed the position where item could appear
            if current.getData() > item:
                return False

            current = current.getNext()

        # Reached the end without finding item
        return False


    def remove(self, item):
        """
        Remove the first occurrence of item.

        This is similar to removing from an unordered linked list,
        but ordered traversal lets us stop early.
        """

        current = self.head
        previous = None

        while current is not None:

            # The item was found
            if current.getData() == item:

                # CASE 1: Remove the head
                if previous is None:
                    self.head = current.getNext()

                # CASE 2: Remove a later node
                else:
                    previous.setNext(current.getNext())

                return

            # Since the list is ordered, the item cannot appear later
            if current.getData() > item:
                return

            previous = current
            current = current.getNext()


    def getList(self):
        """
        Return all values as one space-separated string.

        Example:

            head -> 10 -> 20 -> 30 -> None

        Returns:

            "10 20 30"
        """

        current = self.head
        values = []

        while current is not None:
            values.append(str(current.getData()))
            current = current.getNext()

        return " ".join(values)


# ============================================================
# PART 4: HOW ORDERED add() WORKS
# ============================================================

"""
Suppose the list is:

    head -> 5 -> 15 -> 25 -> 40 -> None

We want to add 20.

Traversal begins with:

    previous = None
    current  = Node(5)

After checking 5:

    previous = Node(5)
    current  = Node(15)

After checking 15:

    previous = Node(15)
    current  = Node(25)

We stop because:

    25 > 20

Therefore, 20 belongs between previous and current:

    previous       newNode       current
        |              |             |
       15             20            25

The connections are changed with:

    newNode.setNext(current)
    previous.setNext(newNode)

Result:

    head -> 5 -> 15 -> 20 -> 25 -> 40 -> None


The same add() method handles all three positions:

1. INSERT AT FRONT

    previous is None
    current is the old head

    Before:
        head -> 5 -> 15 -> None

    Add 2:

        head -> 2 -> 5 -> 15 -> None


2. INSERT IN MIDDLE

    previous and current are both Node objects

    Before:
        head -> 5 -> 15 -> 25 -> None

    Add 20:

        head -> 5 -> 15 -> 20 -> 25 -> None


3. INSERT AT END

    previous is the old final node
    current is None

    Before:
        head -> 5 -> 15 -> 25 -> None

    Add 50:

        head -> 5 -> 15 -> 25 -> 50 -> None
"""


# ============================================================
# PART 5: TESTING THE ORDERED LINKED LIST
# ============================================================

def test_insertIntoOrderedList():
    ll = OrderedLinkedList()

    # Add values in an unsorted order
    ll.add(35)
    ll.add(50)
    ll.add(10)
    ll.add(40)
    ll.add(20)
    ll.add(30)

    # The linked list should automatically maintain ascending order
    assert ll.getList() == "10 20 30 35 40 50"

    # Insert at the front
    ll.add(5)

    assert ll.getList() == "5 10 20 30 35 40 50"

    # Insert at the end
    ll.add(60)

    assert ll.getList() == "5 10 20 30 35 40 50 60"


def test_orderedListSearch():
    ll = OrderedLinkedList()

    ll.add(5)
    ll.add(15)
    ll.add(25)
    ll.add(40)

    assert ll.search(5) is True
    assert ll.search(25) is True
    assert ll.search(40) is True

    assert ll.search(1) is False
    assert ll.search(20) is False
    assert ll.search(50) is False


def test_orderedListRemove():
    ll = OrderedLinkedList()

    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)

    # Remove from the middle
    ll.remove(20)
    assert ll.getList() == "10 30 40"

    # Remove the head
    ll.remove(10)
    assert ll.getList() == "30 40"

    # Remove the final node
    ll.remove(40)
    assert ll.getList() == "30"

    # Remove an item that does not exist
    ll.remove(100)
    assert ll.getList() == "30"

    # Remove the last remaining node
    ll.remove(30)

    assert ll.isEmpty() is True
    assert ll.getList() == ""


# ============================================================
# PART 6: LINKED LIST WITH A TAIL REFERENCE
# ============================================================

"""
A normal linked list only stores a head reference:

    head -> 5 -> 15 -> 25 -> None

Without a tail reference, adding to the end requires starting at
head and traversing the entire list.

That takes O(n).


We can also store a tail reference:

    head -> 5 -> 15 -> 25 -> None
                         |
                        tail

tail always refers to the final Node object.

Now adding to the end takes O(1), because we already have a
reference to the final node.
"""


class LinkedListWithTail:
    def __init__(self):
        # An empty list has no first or final node
        self.head = None
        self.tail = None


    def isEmpty(self):
        return self.head is None


    def addToEnd(self, item):
        """
        Add a new node to the end of the linked list.

        Runtime: O(1)
        """

        newNode = Node(item)

        # CASE 1: The list is empty
        if self.head is None:

            # The first node is both the head and the tail
            self.head = newNode
            self.tail = newNode

        # CASE 2: The list already contains nodes
        else:
            # Connect the old tail to the new node
            self.tail.setNext(newNode)

            # Update tail so it refers to the new final node
            self.tail = newNode


    def getList(self):
        current = self.head
        values = []

        while current is not None:
            values.append(str(current.getData()))
            current = current.getNext()

        return " ".join(values)


# ============================================================
# PART 7: HOW tail WORKS
# ============================================================

"""
Suppose the list is:

    head -> 5 -> 15 -> 25 -> None
                         |
                        tail

We add 30:

    newNode = Node(30)

The new node initially exists separately:

    newNode -> 30 -> None


FIRST:

    self.tail.setNext(newNode)

Because self.tail refers to Node(25), this is equivalent to:

    25.next = newNode

Now the new node is connected:

    head -> 5 -> 15 -> 25 -> 30 -> None

However, tail still refers to Node(25).


SECOND:

    self.tail = newNode

Now tail refers to Node(30):

    head -> 5 -> 15 -> 25 -> 30 -> None
                               |
                              tail


The lines perform two different jobs:

    self.tail.setNext(newNode)  # Connect the old tail
    self.tail = newNode         # Update the tail reference


The order matters.

Incorrect order:

    self.tail = newNode
    self.tail.setNext(newNode)

This would make the new node point to itself and would lose the
connection from the old tail.
"""


# ============================================================
# PART 8: TESTING THE TAIL REFERENCE
# ============================================================

def test_linkedListWithTail():
    ll = LinkedListWithTail()

    assert ll.head is None
    assert ll.tail is None
    assert ll.isEmpty() is True

    # Add the first node
    ll.addToEnd(5)

    # With one node, head and tail refer to the same Node object
    assert ll.head == ll.tail
    assert ll.head.getData() == 5
    assert ll.tail.getData() == 5

    # Add more nodes
    ll.addToEnd(15)
    ll.addToEnd(25)

    assert ll.getList() == "5 15 25"

    # head still refers to the first node
    assert ll.head.getData() == 5

    # tail now refers to the final node
    assert ll.tail.getData() == 25

    # The final node's next reference must be None
    assert ll.tail.getNext() is None


# ============================================================
# PART 9: RUNTIME SUMMARY
# ============================================================

"""
UNORDERED LINKED LIST

Operation                       Runtime
------------------------------------------------
Check if empty                  O(1)
Add to front                    O(1)
Find length                     O(n)
Search                          O(n)
Remove                          O(n)


ORDERED LINKED LIST

Operation                       Runtime
------------------------------------------------
Check if empty                  O(1)
Add while maintaining order     O(n)
Search                          O(n)
Remove                          O(n)

Ordered searching can sometimes stop early, but the worst case
still requires visiting every node, so its runtime remains O(n).


LINKED LIST WITH TAIL

Operation                       Without tail      With tail
------------------------------------------------------------
Add to front                    O(1)              O(1)
Add to end                      O(n)              O(1)


KEY IDEAS

1. head refers to the first Node object.

2. tail refers to the final Node object.

3. A node's next attribute refers to another Node object,
   not directly to the next value.

4. Inserting at the front only changes references, so it is O(1).

5. Ordered insertion is O(n) because we may need to traverse the
   list to find the correct position.

6. Ordered search can stop when current.data becomes greater than
   the target, but its worst-case runtime is still O(n).

7. Keeping a tail reference makes adding to the end O(1).

8. Use:

       x is None
       x is not None

   when checking for None.

9. Use == when comparing ordinary values:

       current.getData() == item

10. Getters and setters:

       node.getData()
       node.getNext()
       node.setData(value)
       node.setNext(otherNode)

    are functionally similar to direct attribute access:

       node.data
       node.next
       node.data = value
       node.next = otherNode

    The lecture uses getters and setters to practice encapsulation.
"""