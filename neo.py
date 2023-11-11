import re

name = input('Enter File: ')
if len(name) < 1:
	name = 'regex_sum_42.txt'
hand = open(name)
sumx = 0
for l in hand:
	numx = re.findall('[0-9]+', l)
	for num in numx:
		sumx += int(num)

print('Sum:', sumx)
