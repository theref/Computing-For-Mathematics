alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blist = [30, 40, 50, 60]
clist = alist + blist
print clist
print len(clist)
print clist[0]
print clist[-1]
print clist[3:12]

place = clist.index(40)
print place
print clist[place:place + 2]