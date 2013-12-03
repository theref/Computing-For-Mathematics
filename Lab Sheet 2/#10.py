textfile = open('mytextfile.txt', 'w')
for i in range(1, 11):
	textfile.write("%s\n" % i)
textfile.close()
