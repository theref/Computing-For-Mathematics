numbers = open('W04_D01.txt', 'r').read().split('\r\n')
numbers = [ int(x) for x in numbers ]
print numbers.index(4558)