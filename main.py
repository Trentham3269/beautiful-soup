#! /usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

# Request the web page
url = 'https://www.smartraveller.gov.au/destinations'
r = requests.get(url)

# Parse the table
s = BeautifulSoup(r.content, "html.parser")
output_rows = []
for row in s.table.tbody.find_all('tr'):
	columns = row.find_all('td')
	output_row = []
	for column in columns:
		output_row.append(column.get_text().strip())
	output_rows.append(output_row)

# Output to csv
with open('output.c sv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)