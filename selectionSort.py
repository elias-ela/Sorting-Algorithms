'''
Selection Sort
	is based on finding the smallest or largest element in a list and
	exchanging it to the first, then finding the second, etc, until the end is
	reached.
Running Time Complexity: O(n^2)
'''

from generate import generateList

def selectionSort(seq):
	'''
	Args:
		seq (list): Iterable of elements to sort.
	Return:
		Sorted list
	'''

	list_length = len(seq)
	for i in range(list_length):
		least = i
		for j in range(i + 1, list_length):
			if seq[j] < seq[least]:
				least = j
		seq[least], seq[i] = seq[i], seq[least]
	return seq

if __name__ == '__main__':
	for i in range(0, 101, 25):
		presortedness = i / 100.00
		seq = generateList(10, presortedness)
		print "\nBefore Selection Sort - presortedness = {}\n".format(presortedness)
		print seq
		print "\nAfter selection Sort\n"
		print selectionSort(seq)
