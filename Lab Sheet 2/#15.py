def iterFib(n):
	"""
	Factorial by iteration

	Inputs: integer

	Outputs: integer!
	"""
	r = 1
	for i in range(1, n + 1):
		r = r * i
	return r

print iterFib(10)

def recurFib(n):
	"""
	Factorial by recursion

	Inputs: integer

	Outputs: integer!
	"""
	return 1 if n == 1 else n * recurFib(n - 1)

print recurFib(10)