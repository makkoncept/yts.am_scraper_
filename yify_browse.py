from bs4 import BeautifulSoup
import requests
import csv
import time

URL = "https://yts.am/browse-movies?page="
csv_file = open('yify_movie_list.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['MOVIES', 'IMDB-RATING'])
for page in range(1, 356):
    time.sleep(1)
    URL = "https://yts.am/browse-movies?page="+str(page)
    r = requests.get(URL).text
    soup = BeautifulSoup(r, "lxml")
    for name in soup.findAll('div', class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"):
        mov_name = name.find('div', class_="browse-movie-bottom")
        movie_name = mov_name.a.text
        print(movie_name)
        rating = name.find('h4', class_="rating").text
        rating = rating[:3]

        if(rating[2] == '/'):
            rating = rating[0:2]
        print(rating)
        print()
        csv_writer.writerow([movie_name, rating])

csv_file.close()
