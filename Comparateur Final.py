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

with open('reservations.csv', 'r') as fd:
	RESV = fd.readlines()
RESV = [x.strip() for x in RESV]
# print(RESV)	
# ^ Crée une list
# ---- 

NTFset = set(NTF)
RESVset = set(RESV)

def returnMatches(NTF, RESV):
	standard = [[x for x in NTF if x not in RESV], [x for x in RESV if x not in NTF]]
	print(standard)

returnMatches(NTF, RESV)