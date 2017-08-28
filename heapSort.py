'''
	Heap Sort
		for every node other than the root, it has at least (at most) the
		value of its parent. Thus, the smallest (largest) element is stored
		at the root and the subtrees rooted at a node contain only larger
		(smaller) values than does the node itself.
	Time Complexity O(nlgn)
'''

from generate import generateList

def heapSort(seq):
	'''
	Args:
		seq (list): Iterable of elements to sort.
	Return:
		Sorted list
	'''

    # convert seq to heap
    length = len(seq) - 1
    leastParent = length / 2
    for i in range (leastParent, -1, -1):
        max_heapify(seq, i, length )

    # flatten heap into sorted list
    for i in range (length, 0, -1):
        if seq[0] > seq[i]:
            seq[0], seq[i] = seq[i], seq[0]
            max_heapify(seq, 0, i - 1)
    return seq

def max_heapify(seq, first, last):
	'''
	Args:
		seq (list): the list tobe sorted.
		first (int): the first index in the list
		last (int): the last index in the list
	Return:
		None
	'''
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (seq[largest] < seq[largest + 1]):
            largest += 1

        # right child is larger than parent
        if seq[largest] > seq[first]:
            seq[largest], seq[first] = seq[first],seq[largest]
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit

if __name__ == '__main__':
	for i in range(0, 25, 25):
		presortedness = i / 100.00
		seq = generateList(5, presortedness)
		print "Before Heap Sort - presortedness = {}\n".format(presortedness)
		print seq
		print "\nAfter Heap Sort\n"
		print heapSort(seq)
