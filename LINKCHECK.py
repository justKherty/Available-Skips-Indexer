import urllib.parse as urlparse
import urllib.request
import csv
import sys, select, os

from urllib.parse import parse_qs


# Pour 5100 skips : 34 min - 10 min

url_start = "http://fondationscp.wikidot.com/scp-"
i = 1

usr = input("Number of articles to check? (Only numbers!)")
usr_int = int(usr)
usr_an = input("Begin from where? (Example : 2000 makes the script begins from SCP-2000)")
usr_an_int = int(usr_an) + 1
print("Script began execution, press Enter to stop script. The data scrapped will be saved.")

def inputter():
	with open('nottranslated.csv', 'a') as csvfile:		
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow([url_real])
		#filewriter.writerow('\n')

for i in range(usr_int):
	u_s_num = usr_an_int
	u_s_num += i
	url_search = str(u_s_num)
	url_real = url_start+url_search
	print(url_real)

	try: 
		urllib.request.urlopen(url_real)
	except urllib.error.HTTPError as e:
		print(e.code)
		e.code = 4e4
		if 4e4 == 404:
			 print(url_real)
		else:
			inputter()

	except urllib.error.URLError as e:
		print(e.args)
		print("URL ERROR")
	else:
		print("OK!")



