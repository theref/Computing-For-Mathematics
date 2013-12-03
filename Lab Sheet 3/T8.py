import timeit

numbers = open('W04_D01.txt', 'r').read().split('\r\n')
numbers = [ int(x) for x in numbers ]
numbers.sort()

binary = timeit.Timer('binarysearch(numbers, 4221)', 'from T7 import binarysearch; numbers=%r' % (numbers))
seq = timeit.Timer('seqsearch(numbers, 4221)', 'from T6 import seqsearch; numbers=%r' % (numbers))

print binary.timeit(100000)
print seq.timeit(100000)

