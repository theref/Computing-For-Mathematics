import csv

out = open("W05_D01.csv", "r")
data = csv.reader(out)
d = [row for row in data]
out.close
data = [[eval(row[0]), eval(row[1]), eval(row[2])] for row in d[1:]]
print data

class Quadratic():
	a = 0
	b = 0
	c = 0

listofquadratics = []
for row in d:
	q = Quadratic
	q.a = row[0]
	q.b = row[1]
	q.c = row[2]
	listofquadratics.append(q)

print listofquadratics