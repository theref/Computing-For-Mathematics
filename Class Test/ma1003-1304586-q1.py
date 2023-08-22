def fib(n):
    """
    A function to give the nth fibonacci number using recursion
 
    Arguments: n, an integer
 
    Outputs: the nth fibonacci number
    """
    return 1 if n in [0, 1] else fib(n - 1) + fib(n - 2)
 
print "The first 10 fibonacci numbers:"
 
for i in range(11):  # Printing the first 10 numbers
    print "f(%s)=%s" % (i, fib(i))