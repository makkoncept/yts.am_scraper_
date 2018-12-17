import csv
import webbrowser
import time

year = 2017
down = 1000
rate = '8.0'
year = int(input("enter year [ 1950 - 2018] "))
down = int(input("enter min number of downloads "))
rate = str(float(input("rate [ 0.0 - 10.0 ] ")))
with open('data.csv', 'r') as open_file:
	open_file.readline()
	open_file.readline()
	c = 0
	l = list()
	for row in csv.reader(open_file):
		if(row[1]>rate and int(row[3])>down and int(row[0].split("(")[1].split(")")[0]) >= year): # rating and number of downloads and year
			if(row[6] == 'null'):
				l.append(row[5])
			else:
				l.append(row[6])
			print(row)
			print(" ")
			c = c + 1

	print(l)
	print(" ")
	print(c)
for i in l:
	webbrowser.open(i)
	if(c%25 == 0):
		time.sleep(10)
	c = c + 1
