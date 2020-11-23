import urllib.parse as urlparse
import urllib.request
import csv
from urllib.parse import parse_qs

url_start = "http://fondationscp.wikidot.com/scp-"
u_s_num = 1

def inputter():

	with open('nottranslated.csv', 'a') as csvfile:		
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow([url_real])
		filewriter.writerow('\n')

for i in range(10000):
	u_s_num = 100
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

