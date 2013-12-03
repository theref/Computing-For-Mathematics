import csv
f = open('classtestdata.csv', 'r')
testnames = csv.reader(f)		# use the csv library to read the file
namelist = [row for row in testnames]		# put all the names into a list
f.close()

namelist = sum(namelist, [])		# removes the awkward 'lists within a list'
length = sum(len(s) for s in namelist)		# finds the total number of letters
nameset = set(namelist)		# converts namelist to a set to remove duplicates

print "There are %s names in the data" % (len(namelist))	# just the length of the list
print "The mean length of a name is %s" % (length/float(len(namelist)))	# total number of letters divided number of names is the mean
print "There are %s unique names in the data" % (len(nameset))	# length of the set ie. without duplicates