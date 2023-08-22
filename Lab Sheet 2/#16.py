def Fib(n):
	if n == 1:
		return 1
	return 1 if n == 2 else Fib(n - 1) + Fib(n - 2)

print Fib(10)