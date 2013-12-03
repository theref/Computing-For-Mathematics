import random

class Drop():
	def __init__(self, r=1):
		self.x = (.5 - random.random()) * 2 * r
		self.y = (.5 - random.random()) * 2 * r
		self.incircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2

def approxpi(N=1000):
	blist =[]
	for i in range(N):
		i = Drop()
		if i.incircle:
			blist.append(i)
	print (len(blist)/float(N))*4

approxpi(500000)