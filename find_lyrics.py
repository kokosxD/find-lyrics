import requests as rq
from bs4 import BeautifulSoup as bs
song = input("Enter song: ")

# Making the parameters for the url
url_params = {"q": song.lower()}

# Making a get request to the azlyric's search ulr + passing the above parameters to it
azlyrics_search = rq.get("https://search.azlyrics.com/search.php", params=url_params)
soup = bs(azlyrics_search.text, "lxml")

# Get a list with all the results for the specific search
search_results = soup.find_all("table", {"class": "table table-condensed"})[-1].find_all("td", {"class": "text-left visitedlyr"})

# Take the first result from the search as the url with the lyrics on it
lyrics_url = search_results[0].a.get("href")
lyrics_page = rq.get(lyrics_url)
soup = bs(lyrics_page.text, "lxml")

# Find the lyrics
lyrics = soup.find("div", {"class": "col-xs-12 col-lg-8 text-center"}).find_all("div")[6].get_text()

# Make a list with every line of the lyrics as a element and remove the first 2 because are html notes
lines = lyrics.splitlines()[2:]
processed_lyrics = "\n".join(lines)
print(processed_lyrics)
