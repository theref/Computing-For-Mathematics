from Tickable1 import jumbledlist

def bubblesort(data):
	firstunsorted = 0
	swap = True
	while firstunsorted < len(data) - 1 and swap:
		swap = False
		index = len(data) - 1
		while index > firstunsorted:
			if data[index] < data[index - 1]:
				data[index], data[index - 1] = data[index - 1], data[index]
				swap = True
			index -= 1
	return data

jlist = jumbledlist(30, 20)
print jlist
print bubblesort(jlist)