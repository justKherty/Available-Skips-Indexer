import re 
import csv
import urllib
import html

#Defining variables

default_url = "http://fondationscp.wikidot.com/scp-"
output = []
cleaned = []

#Main function, to append the data from the CSV file final reservations, to the default_url link, dynamically 

def unifier():
	with open("final_reservations.csv", 'r+') as frc:
		csv_reader = csv.reader(frc, delimiter='\n')
		for line in frc:
			output = [default_url + line for line in frc]
			#print(output)
			output = [re.sub(r"[\[\]]", r"'", "", output) for line in frc]
			print(output)
unifier()

def cleaner():
	with open("final_final.csv", 'w') as frc2:
		csv_reader = csv.reader(frc2, delimiter='\n')
		for line in frc2:
			check1 = [re.sub(r"[\[\]]", "", output)]
			print(check1)
cleaner()