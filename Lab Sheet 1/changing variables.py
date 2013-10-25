f = 9.42345
print round(f, 2)
print float(int(f))
s = str(f)
print s
print type(s)


numberofcats = 0
name = "James"
height = 1.72
notborn = "Wales"

string = "My name is " + name +", I am " + str(height) + " metres tall, have " + str(numberofcats) + " cats and was not born in " + notborn
newstring = "My name is %s, I am %.1f metres tall, have %i cats and was not born in %s" % (name, height, numberofcats, notborn)

print string
print newstring