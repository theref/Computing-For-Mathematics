goodphonebook = {
				"Vince": 3,
				"Zoe": 2,
				"Julien": 6,
				"Thomas": 10,
				"Mike": 1,
				"Matt": 4
				}

print goodphonebook.get("Thomas")
print goodphonebook.get("Brayden")
print goodphonebook.get("Brayden", 'Not in book')
print goodphonebook.get("Thomas", 'Not in book')

print goodphonebook['Vince']
goodphonebook['Vince'] = 8
print goodphonebook['Vince']

print goodphonebook['Brayden']