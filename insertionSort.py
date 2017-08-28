'''
	Insertion Sort
		is a simple sorting algorithm with average and worst runtime cases of
		O(n^2). It sorts by repeatedly inserting the next unsorted element in
		an initial sorted segment of the list.
'''

from generate import generateList

def insertionSort(seq):
	'''
	Args:
		seq (list): Iterable of elements to sort.
	Return:
		Sorted list
	'''

	for i in range(len(seq)):
		key = seq[i]
		j = i - 1
		while (j >= 0) and (seq[j] > key):
			seq[j + 1] = seq[j]
			j -= 1
		seq[j + 1] = key
	return seq

if __name__ == '__main__':
	for i in range(0, 101, 25):
		presortedness = i / 100.00
		seq = generateList(10, presortedness)
		print "Before Insertion Sort - presortedness = {}\n".format(presortedness)
		print seq
		print "\nAfter Insertion Sort\n"
		print insertionSort(seq)
