with open('mytextfile.txt', 'w') as textfile:
	for i in range(1, 11):
		textfile.write("%s\n" % i)
