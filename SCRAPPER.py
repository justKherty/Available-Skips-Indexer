import urllib.request
import csv
from bs4 import BeautifulSoup

url = "http://fondationscp.wikidot.com/traductions-reservees"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page)

# project_href = [i['href'] for i in soup.find_all('a', href=True)]
# ph = [i['href'] for i in soup.find_all(href=True)]
ph2 = soup.find_all('a', class_="newpage")

# print(project_href)
print(ph2)

with open('reservations.csv', 'w') as myfile:
	for line in ph2:
    		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    		wr.writerow([line])
    		wr.writerow('\n')
		



