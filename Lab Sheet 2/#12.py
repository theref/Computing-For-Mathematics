def isprime(n):
	"""
	Checks if an integer is prime

	Arguments: any integer

	Outputs: Boolean value
	"""
	return max([e % n for e in range(2, n)]) != 0

numbers = open('W03_D01.txt', 'r').read().split('\n')
numberlist = [int(e) for e in numbers[:-1]]

primeset = set()
for i in numberlist:
	if isprime(i):
		primeset.add(i)

print len(primeset)




