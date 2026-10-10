'''Binary Search'''

# Binary search finds a target in a SORTED list.
# Instead of checking every element, it removes
# about half of the remaining elements each step.

# Runtime: O(log n)



def binarySearch1(intList, item):  #bool version iterative
	first = 0
	last = len(intList) - 1
	found = False

	while first <= last and not found:
		mid = (first + last) // 2
		if intList[mid] == item:
			found = True
		else:
			if item < intList[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found



def binarySearch2(intList, item):           #recursive bool
	if len(intList) == 0: # base case
		return False

	mid = len(intList) // 2
	if intList[mid] == item:
		return True
	elif item < intList[mid]:
		return binarySearch2(intList[0:mid], item)
	else:
		return binarySearch2(intList[mid+1:], item)





    
def binary_search3(intList, target):            # returns the index recursive version

    def search(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if target == intList[mid]:
            return mid
        elif target < intList[mid]:
            return search(low, mid - 1)
        else:
            return search(mid + 1, high)

    return search(0, len(intList) - 1)



def binary_search4(intList, target, low, high):            # returns the index recursive version

        if low > high:
            return -1

        mid = (low + high) // 2

        if target == intList[mid]:
            return mid
        elif target < intList[mid]:
            return binary_search4(intList, target, low, mid-1)
        else:
            return binary_search4(intList, target, mid+1, high)


nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

print(binary_search4(nums, 12, 0, len(nums) - 1))