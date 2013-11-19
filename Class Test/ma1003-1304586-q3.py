import random

class Drop():
	"""
    A class for a rain drop falling in a random location on a square
 
    Attributes:
        x: the x coordinate of the point
        y: the y coordinate of the point
        underline: a boolean indicating whether or not the point is underneatht the line y = 1 - (x ** 2)
    """
	def __init__(self, r=1):
		self.x = random.random()
		self.y = random.random()
		self.underline = self.y <= 1 - (self.x) ** 2	# This returns the boolean corresponding to whether or not the point is underneatht the line y = 1 - (x ** 2)

def approxarea(N=1000):
	"""
	A function to approximate the probability of a drop landing underneath a given curve
	Arguments: N (default=1000) which is the number of points
	Outputs: The probability as a float
	"""
	alist =[]
	for i in range(N):
		i = Drop()			# creates an instance of the class Drop
		if i.underline:		#checks if the instance is under the line or not
			alist.append(i)		# puts those points that return True into a list
	return (len(alist)/float(N))	# returns the length of the list divided by the total number of Drops, hence the probability

print "The approximate area under the line y = 1 - (x ** 2) in the range [0,1] is %s" % (approxarea(50000))