import csv
import webbrowser
with open('yify_movie_list.csv', 'rb') as open_file:
	open_file.readline()
	for row in csv.reader(open_file):
		webbrowser.open(row[6])