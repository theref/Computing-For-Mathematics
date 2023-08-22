def iterX(n):
	"""
	An iterative approach

	Inputs: integers

	Outputs: integers
	"""
	r = 1
	for _ in range(n - 1):
		r *= 2
	return r

print iterX(4)

def recX(n):
	"""
	A recursive approach

	Inputs: integers

	Outputs: integers
	"""
	return 1 if n == 1 else 2 * recX(n - 1)

print recX(4)