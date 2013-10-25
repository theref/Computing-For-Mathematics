def numbers(n):
	power = str(n ** n)
	end = str(n) * 2
	length = len(str(n) * 2)
	while end in power:
		if power.rfind(end) == (len(power) - len(end)):
			return n