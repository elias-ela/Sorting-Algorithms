'''
    Bubble Sort
        start from the beginning or the end of the list and check if the
        value that is next or previous to it and then swap if the value is less
        or greater depending on where you start.
'''

from generate import generateList

def bubbleSort(seq):
	'''
	Args:
		seq (list): Iterable of elements to sort.
	Return:
		Sorted list
	'''

    size = len(seq) - 1
    for _ in range(size):
        for i in range(size):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq

if __name__ == '__main__':
	for i in range(0, 101, 25):
		presortedness = i / 100.00
		seq = generateList(10, presortedness)
		print "\nBefore Bubble Sort - presortedness = {}\n".format(presortedness)
		print seq
		print "\nAfter Bubble Sort\n"
		print bubbleSort(seq)
