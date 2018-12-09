import csv
import webbrowser
import time
with open('yify_movie_list.csv', 'rb') as open_file:
	open_file.readline()
	c = 0
	for row in csv.reader(open_file):
		webbrowser.open(row[6])
		if(c%25 == 0):
			time.sleep(10)
		c = c + 1
