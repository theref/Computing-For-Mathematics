numbers = open('W04_D01.txt', 'r').read().split('\r\n')
numbers = [ int(x) for x in numbers ]
numbers.sort()
targets = [19, 592, 9507, 4221]

def recurbinary(data, item, lower = 0, upper = -1):
	upper = data.index(data[upper])
	middle = int((upper + lower) / 2)
	if data[lower] > item or data[upper] < item:
		return "item not in list"
	if data[middle] == item:
		return middle
	elif data[middle] > item:
		upper = middle - 1
	elif data[middle] < item:
		lower = middle + 1
	return recurbinary(data, item, lower, upper)

for i in targets:
	print recurbinary(numbers, i)