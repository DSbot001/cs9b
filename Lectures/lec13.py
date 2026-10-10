def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2

		# uses additional space to create the left / right
		# halves
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		# recursively sort the lefthalf, then righthalf
		mergeSort(lefthalf)
		mergeSort(righthalf)

		# merge two sorted sublists (left / right halves)
		# into the original list (alist)
		i = 0 # index for lefthalf sublist
		j = 0 # index for righthalf sublist
		k = 0 # index for alist

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				alist[k] = lefthalf[i]
				i = i + 1
			else:
				alist[k] = righthalf[j]
				j = j + 1
			k = k + 1

		# put the remaining lefthalf elements (if any) into
		# alist
		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		# put the remaining righthalf elements (if any) into
		# alist
		while j < len(righthalf):
			alist[k] = righthalf[j]
			j = j + 1
			k = k + 1



# Merge Sort breaks the list into two equal parts per recursive iteration
# Note that the height (number of levels) of the tree is log n (for 8 nodes, we have a height of 3).
# For each level, the merge step needs to compare n elements
# So if there are log n levels and we need to do n comparisons to merge the elements for each level, then we have: O(n log n) running time
# One disadvantage of Merge Sort is it requires O(n) additional space when creating the left and right sublists      Can be problematic if the list we’re trying to sort is extremely large