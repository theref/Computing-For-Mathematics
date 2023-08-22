def function(n):
	"""
	Does the function described in tickable 5.

	Arguments: any integer

	Outputs: other integers depending on the inputs properties
	"""
	if n % 2 == 1: # if n is odd return n cubed
		return n ** 3
	return (n ** 2) + 1 if n % 4 == 0 else n - 1

mylist = [function(i) for i in range(101)]
print mylist