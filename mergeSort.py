'''
	Merge Sort
		divides the seq in half to create two unsorted lists. These two
		unsorted lists are sorted and merged by continually calling the
		Merge-sort algorithm, until it reeaches a list size of 1.
	Time Complexity O(nlgn)
'''

from generate import generateList

def mergeSort(seq):
	'''
	Args:
		seq (list): Iterable of elements to sort.
	Return:
		Sorted list
	'''

	if len(seq) < 2:
		return seq
	mid = len(seq) // 2
	left = mergeSort(seq[:mid])
	right = mergeSort(seq[mid:])
	i,j,k = 0,0,0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			seq[k] = left[i]
			i += 1
		else:
			seq[k] = right[j]
			j +=1
		k += 1
	while i < len(left):
		seq[k] = left[i]
		i,k = i + 1, k + 1
	while j < len(right):
		seq[k] = right[j]
		j,k = j + 1, k + 1
	return seq

if __name__ == '__main__':
	for i in range(0, 101, 25):
		presortedness = i / 100.00
		seq = generateList(10, presortedness)
		print "Before Merge Sort - presortedness = {}\n".format(presortedness)
		print seq
		print "\nAfter Merge Sort\n"
		print mergeSort(seq)
