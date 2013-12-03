print range(0, 10, 3)

#11
s = 0
for i in range(1001):
	if i % 3 != 0:
		s += i
print s

#13
k = 0
i = 0
while k <= 20000:
	k += i ** 2
	i += 1
print "N=" + str(i)

#14
print "find square root of?"
k = float(raw_input())
print "number of iterations?"
precision = int(raw_input())
X = 1
count = 0
while count <= precision:
	X = (X + k / X) / 2
	count += 1
print X
