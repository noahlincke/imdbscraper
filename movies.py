import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

year=input("What year: ")

numMovies=int(input("How many movies: "))

url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"

ourUrl = urllib3.PoolManager().request('GET', url).data

soup = BeautifulSoup(ourUrl, "lxml")

print(soup.find('title').text)

i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for div_item in movieList:
	if i<=numMovies:
	    div = div_item.find('div',attrs={'class':'lister-item-content'})
	    print(str(i) + '.', end=" ")
	    header = div.findChildren('h3',attrs={'class':'lister-item-header'})
	    print(str((header[0].findChildren("a"))[0].contents[0].encode("utf-8").decode("ascii", "ignore")))
	    i += 1