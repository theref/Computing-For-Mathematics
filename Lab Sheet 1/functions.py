# 17, 18
def mydiv(a, b): 
	if b != 0:
		print float(a) / float(b)
	else:
		print "cannot divide by 0"
mydiv(11, 5)

# 19
def sumk(K = 5, B = 3):
	total = 0
	for i in range(K + 1):
		if i % B != 0:
			total += i
	print total

sumk()

# 21
def fibonacci(N):
	a = 0
	b = 1
	count = 0
	while count <= N:
		fib = b
		b = b + a
		a = fib
		count += 1
	print fib
fibonacci(10)