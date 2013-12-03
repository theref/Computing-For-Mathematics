import csv

ifile = open('W05_D01.csv', "rb")
reader = csv.reader(ifile)

class Quadratic():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def roots(self):
		if (int(self.b) ** 2) - (4 * int(self.a) * int(self.c)) >= 0:
			return True
		else:
			return False

def createquad(alist):
	quadlist = []
	for i in alist:
		i = Quadratic(i[0], i[1], i[2])
		quadlist.append(i)
	return quadlist

quads = createquad(reader)
newlist = [ i for i in quads[1:] if i.roots()]
print len(newlist)