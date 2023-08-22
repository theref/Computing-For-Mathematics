numbers = open('W04_D01.txt', 'r').read().split('\r\n')
numbers = [ int(x) for x in numbers ]
numbers.sort()
targets = [19, 592, 9507, 4221]

def seqsearch(data, item):
	"""
	Find an item using sequential seqsearch
	Inputs: the data, the item to be found
	Outputs: the index of the item or an error message
	"""
	index = 0
	found = False
	while index < len(data) and data[index] <= item and not found:
		if data[index] == item:
			found = True
		else:
			index += 1
	return index if found else "item not in list"


#for i in targets:
	#print seqsearch(numbers, i)

