textfile = open('mytextfile.txt', 'r')
string = textfile.read()
print string

data = string.split('\n')
data = [int(e) for e in data[:-1]]
print data