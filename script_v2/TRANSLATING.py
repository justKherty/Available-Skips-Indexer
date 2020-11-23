import re
import csv
import itertools
import operator

# Array generator

with open('nottranslated.csv', 'r') as fd:
	NONTRADUIT = fd.readlines()
NONTRADUIT = [x.strip() for x in NONTRADUIT]
# print(NONTRADUIT)	

# ^ Crée une list

# -----
 
listcheck = ['']

check = [re.sub(r'\W', '', i) for i in NONTRADUIT]
# print(check)

def inputter():
	with open('not_translated_final.csv', 'a', newline='\n') as csvfile:		
		filewriter = csv.writer(csvfile, dialect='excel')
		filewriter.writerow([check5])

final = []

for i in check:
	if True:
		final.append(i)
	else:
		pass

# print(final)

check2 = [re.sub('[http://fondationscp.wikidot.com/scp-]', '', i) for i in NONTRADUIT]
# print(check2)
check3 = [item for item in check2 if item != '']
# print(check3)
check4 = [item.replace("|", "") for item in check3]
print(check4)
check5 = [list(filter(None, check4))] 
print(check5)

for item in check5:
	check6 = "".join(dict.fromkeys(check5))
	print(check6)
	inputter()
