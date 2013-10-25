def jumbledlist(maxnum, size):
	"""
	Returns a list of random integers

	Inputs: maxnum-the largest integer allowed
			size-the length of the list

	Outputs: a list of random integers
	"""
	import random
	return random.sample(range(1, maxnum), size)

print jumbledlist(100, 10)