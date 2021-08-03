#United Script Attempt 1
#
#First script: SCRAPPER
#Second script: NETTOYEUR
#

import re
import csv
import itertools
import operator
import urllib.request
import csv
from bs4 import BeautifulSoup

url = "http://fondationscp.wikidot.com/traductions-reservees"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page)
ph2 = soup.find_all('a', class_="newpage")

print(ph2)

with open('reservations.csv', 'w') as myfile:
	for line in ph2:
    		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    		wr.writerow([line])
    		wr.writerow('\n')

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
check5 = [re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', '', i) for i in check4]
#print(check5)

def inputter():
	with open('final_reservations.csv', 'a', newline='\n') as csvfile:		
		filewriter = csv.writer(csvfile, dialect='excel')
		filewriter.writerow([real_final])

f3c = []
f4c = []

final = []
stripped = []

for i in check5:
	sep = 'P'

	if len(i)==9:
		final.append(i)

	elif len(i)==11:
		final.append(i)

	else:
		pass

real_final = []
rrfinal = []

for item in final:
	real_final = [re.sub("\A(\d+)S.*\Z", r"\1", item)]
	print(real_final)
	inputter()