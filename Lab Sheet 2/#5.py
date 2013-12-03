def function(n):
	"""
	Does the function described in tickable 5.

	Arguments: any integer

	Outputs: other integers depending on the inputs properties
	"""
	if n % 2 == 1: # if n is odd return n cubed
		return n ** 3
	if n % 4 == 0: # if n is divisible by 4, return n squared plus 1
		return (n ** 2) + 1
	else: # otherwise return n-1
		return n - 1

mylist = [function(i) for i in range(101)]
print mylist