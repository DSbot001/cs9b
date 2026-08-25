'''Quicksort, Trees'''

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist) - 1)

# helper function so we can pass in the first / last index
# of lists


def quickSortHelper(alist, first, last):
	if first < last:

		# will define the indices of the left / right sub lists
		splitpoint = partition(alist, first, last)

		# recursively sort the left / right sub lists
		quickSortHelper(alist, first, splitpoint-1) # left of pivot
		quickSortHelper(alist, splitpoint+1, last) # right of pivot

# partition function will organize left sublist < pivot
# and right sub list > pivot



def partition(alist, first, last):
	pivotvalue = alist[first] # choose first element as pivot

	leftmark = first + 1
	rightmark = last

	done = False
	while not done:

		# move leftmark until we find a left element > pivot
		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		# move rightmark until we find a right element < pivot
		while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
			rightmark = rightmark - 1

		# check if we're done swapping left / right elements in
		# correct side
		if rightmark < leftmark:
			done = True
		else: # swap left and right elements into correct side of list
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	# put the pivot value into the correct place (swap pivot w/ rightmark)
	temp = alist[first] # pivot
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark






'''QUICKSORT RUNTIME'''

# partition() scans through the current section of the list.
# leftmark moves right and rightmark moves left.
# Together, they process about n elements.
# Therefore:
# partition = O(n)

# GOOD / AVERAGE CASE:
# If the pivot divides the list roughly in half:
#
#              n
#           /     \
#         n/2     n/2
#        /  \     /  \
#      n/4 n/4  n/4 n/4
#
# Each layer does about O(n) total work.
# There are about O(log n) layers.
#
# Runtime = O(n) * O(log n)
#         = O(n log n)


# WORST CASE:
# If the pivot is always the smallest/largest element:
#
# n
#  \
#  n-1
#    \
#    n-2
#      \
#      ...
#
# Work = n + (n-1) + (n-2) + ... + 1
#      = O(n^2)
#
# Quicksort:
# Average / good case: O(n log n)
# Worst case:          O(n^2)


'''TREES'''

# A tree is a non-linear data structure made of connected nodes.
#
#                 A          <- root
#               /   \
#              B     C       <- children of A
#             / \     \
#            D   E     F     <- leaves
#
# Root:
#   The top node of the tree.
#
# Parent / Child:
#   A is the parent of B and C.
#   B and C are children of A.
#
# Siblings:
#   Nodes with the same parent.
#   B and C are siblings.
#
# Leaf:
#   A node with no children.
#   D, E, and F are leaves.
#
# Edge:
#   A connection between two nodes.
#
# Path:
#   A sequence of connected nodes.
#   Example: A -> B -> D
#
# Depth:
#   Number of edges from the root to a node.
#   root depth = 0
#
# Height:
#   How deep the tree goes (based on the longest root-to-leaf path).
#
# Subtree:
#   A node and all of its descendants form another smaller tree.


'''BINARY TREES'''

# A binary tree is a tree where each node has
# AT MOST two children:
#
#             A
#           /   \
#          B     C
#          ^     ^
#        left   right
#
# A node may have:
# 0 children
# 1 child
# 2 children
#
# Trees are naturally recursive:
#
#             tree
#            /    \
#      left tree  right tree
#
# Each subtree is itself another tree.


'''BFS VS DFS - EXTRA'''

# BFS = Breadth-First Search
# - Visits nodes level by level
# - Usually uses a QUEUE (FIFO)
#
#             A
#           /   \
#          B     C
#         / \   / \
#        D   E F   G
#
# BFS: A -> B -> C -> D -> E -> F -> G


# DFS = Depth-First Search
# - Goes down one path before coming back
# - Usually uses a STACK or RECURSION
#
# One possible DFS:
# A -> B -> D -> E -> C -> F -> G
#
# Remember:
# BFS -> breadth -> Queue
# DFS -> depth   -> Stack / Recursion