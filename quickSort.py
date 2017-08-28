'''
	Quick sort
		works by choosing a pivot and partitioning the array so that the
		elements that are smaller than the pivot go to the left, and elements
		that are larger go to the right. Then, it recursively sorts these left
		and right parts.
	Time Complexity O(n^2)
'''

from generate import generateList

def quickSort(seq):
	'''
	Args:
		seq (list): Iterable of elements to sort.
	Return:
		Sorted list
	''''

	if len(seq) <= 1:
		return seq
	else:
		return quickSort([x for x in seq[1:] if x < seq[0]]) + \
				[seq[0]] + \
				quickSort([x for x in seq[1:] if x >= seq[0]])

if __name__ == '__main__':
	for i in range(0, 101, 25):
		presortedness = i / 100.00
		seq = generateList(10, presortedness)
		print "Before Quick Sort - presortedness = {}\n".format(presortedness)
		print seq
		print "\nAfter Quick Sort\n"
		print quickSort(seq)





















# def partition(list, first, last):
# 	pivot = last
# 	store_index = first - 1
# 	for i in xrange(first, last):
# 		if list[i] < pivot:
# 			store_index += 1
# 			list[i], list[store_index] = list[store_index], list[i]
# 	list[store_index + 1], list[last] = list[last], list[store_index + 1]
# 	return store_index + 1

# 	# pivot = list[first]
# 	# left = first + 1
# 	# right = last
# 	# done = False

# 	# while not done:
# 	# 	while left <= right and list[left] <= pivot:
# 	# 		left += 1
# 	# 	while list[right] >= pivot and right >= left :
# 	# 		right -= 1
# 	# 	if right < left:
# 	# 		done = True
# 	# 	else:
# 	# 		list[left], list[right] = list[right], list[left]
# 	# list[first], list[right] = list[right], list[first]

# 	# return right

# def quickSort(list, first, last):
# 	if first < last:
# 		mid = partition(list, first, last)
# 		quickSort(list, first, mid - 1)
# 		quickSort(list, mid + 1, last)
# def partition(list, first, last):
# 	pivot = list[first]
# 	left = first + 1
# 	right = last
# 	done = False

# 	while not done:
# 		while left <= right and list[left] <= pivot:
# 			left += 1
# 		while list[right] >= pivot and right >= left :
# 			right -= 1
# 		if right < left:
# 			done = True
# 		else:
# 			list[left], list[right] = list[right], list[left]
# 	list[first], list[right] = list[right], list[first]

# 	return right

# def quickSort(list, first, last):
# 	if first < last:
# 		mid = partition(list, first, last)
# 		quickSort(list, first, mid - 1)
# 		quickSort(list, mid + 1, last)
