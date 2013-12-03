str1 = "This is a string that I will learn to manipulate"
str2 = ", string manipulation is very useful."
string = str1 + str2
print string
print len(string)
print string[0]
print string[-1]
print string[3:7]

start = str1.index("string")
print start
print str1[start:start + len("string")]
# .index will return the index of its parameter providing it can be found.
# start:start + len("string") is a range like line 8