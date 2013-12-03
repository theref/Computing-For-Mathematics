numbers = open('W04_D01.txt', 'r').read().split('\r\n')
numbers = [ int(x) for x in numbers ]
numbers.sort()
targets = [19, 592, 9507, 4221]

def binarysearch(data, item):
	"""
	Finds an item using binary sort
	Inputs: the data and the item to be found
	Outputs: the index of the item
	"""
	first = 0
	last = len(data) - 1
	found = False
	if data[first] > item or data[last] < item:
		return "item not in list"
	while first <= last and not found:
		middle = int((first + last) / 2) # gets the middle index by finding the mean
		if item == data[middle]: # checks if the middle term is the item
			found = True
		elif first == last and not found:
			return "item not in list"
		elif item < data[middle]: #checks if the middle term is more than the item
			last = middle - 1 # changes the last index to 1 less than middle index
		else: # assumes that item must be more than middle
			first = middle + 1 # changes the first index to 1 more than middle index
	return middle

#for i in targets:
	#print binarysearch(numbers, i)