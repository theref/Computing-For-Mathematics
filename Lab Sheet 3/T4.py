import time

def timing(string, N):
	"""
	Returns the time a function took to complete
	Inputs: name of a function, number of times to repeat it
	Outputs: the mean time taken
	"""
	totaltime = 0
	for _ in range(N):
		starttime = time.time()
		eval(string)
		totaltime += time.time() - starttime
	return (totaltime / float(N))

def testfunction():
	k = 0
	while k < 10 ** 6:
		k += 1

print timing("testfunction", 1)
print timing("testfunction", 10)
print timing("testfunction", 100)
print timing("testfunction", 1000)
print timing("testfunction", 10000)
print timing("testfunction", 10000000000)