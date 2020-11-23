import re
import csv
import itertools
import operator

# Array generator

with open('reservations.csv', 'r') as fd:
	content = fd.readlines()
content = [x.strip() for x in content]
# print(content)	

# ^ Crée une list

# -----
 
listcheck = ['']

check = [re.sub(r'\W', '', i) for i in content]
# print(check)
check2 = [re.sub('[aclassnewpagehref]', '', i) for i in check]
# print(check2)
check3 = [re.sub('[/<=""]', '', i) for i in check2]
# print(check3)
check4 = [item for item in check3 if item != '']
# print(check4)

def inputter():
	with open('final_reservations.csv', 'a', newline='\n') as csvfile:		
		filewriter = csv.writer(csvfile, dialect='excel')
		filewriter.writerow([real_final])
		# filewriter.writerow('\n')

f3c = []
f4c = []

final = []
stripped = []

for i in check4:
	sep = 'P'

	if len(i)==9:
		final.append(i)

	elif len(i)==11:
		final.append(i)

	else:
		pass

# print(final)

real_final = []
rrfinal = []

for item in final:
	real_final = [re.sub("\A(\d+)S.*\Z", r"\1", item)]
	print(real_final)
	inputter()



