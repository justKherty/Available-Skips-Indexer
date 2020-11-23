import re
import csv
import itertools
import operator

# Array generator // Articles Non-Traduits

with open('not_translated_final.csv', 'r') as fd:
	NTF = fd.readlines()
	NTF = [x.strip() for x in NTF]
# print(NTF)
# ^ Crée une list

# ----
# Array generator // Articles réservés

with open('final_reservations.csv', 'r') as fd:
	RESV = fd.readlines()
	RESV = [x.strip() for x in RESV]
# print(RESV)
# ^ Crée une list
# ----

# NTFset = set(NTF)
# RESVset = set(RESV)

#def returnMatches(NTF, RESV):

def INDEX():
        for i in nomatch:
                with open('complex.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerow([nomatch])

# def returnMatches(NTF, RESV):
#	standard = [[x for x in NTF if x in RESV], [x for x in RESV if x in NTF]]
#	print(standard)
#returnMatches(NTF, RESV)

def NoMatchingDef(NTF, RESV):
	nomatch = []
	for i in NTF:
		if i not in RESV:
			nomatch.append(i)
	return nomatch

nomatch = NoMatchingDef(NTF, RESV)
print(nomatch)

INDEX()

