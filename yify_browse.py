from bs4 import BeautifulSoup
import requests
import csv

URL = "https://yts.am/browse-movies?page="
csv_file = open('yify_movie_list.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['MOVIES', 'IMDB-RATING', 'NUMBER OF LIKES', 'NUMBER OF DOWNLOADS','IMDb Link'])
for page in range(1, 357):
    URL = "https://yts.am/browse-movies?page="+str(page)
    r = requests.get(URL).text
    soup = BeautifulSoup(r, "lxml")
    for name in soup.findAll('div', class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"):
        mov_name = name.find('div', class_="browse-movie-bottom")
        movie_name = mov_name.a.text
        movie_year = mov_name.div.text
        movie_name = movie_name + " " + movie_year

        rating = name.find('h4', class_="rating").text
        rating = rating[:3]

        if(rating[2] == '/'):
            rating = rating[0:2]

        try:
            movie_url = "https://yts.am/movie/" + movie_name.replace(" ", "-")
            movie_url = movie_url.lower()
            request = requests.get(movie_url).text
            n_soup = BeautifulSoup(request, "lxml")
            info = n_soup.find('div', class_="bottom-info")
            likes = info.find('span', id="movie-likes").text
            imdb_link = info.find('a', title="IMDb Rating")['href']
            downladed = n_soup.find('div', id="synopsis")
            downloaded = downladed.find('p', class_=None)
            for down_loaded in downloaded.findAll('em'):
                if(down_loaded.text[:10] == 'Downloaded'):
                    num_downloads = down_loaded.text[11:]
                    num_downloads = num_downloads[:(len(num_downloads)-6)]

        except Exception as e:
            likes = None
            num_downloads = None
            imdb_link = None
            pass
        movie_name = mov_name.a.text + " (" + movie_year + ")"
        print(movie_name)
        print("imdb rating:", rating)
        print("number of likes:", likes)
        print("number of downloads:", num_downloads)
         print("IMDb link:", imdb_link)
        csv_writer.writerow([movie_name, rating, likes, num_downloads, imdb_link])

print("done !!")
csv_file.close()
