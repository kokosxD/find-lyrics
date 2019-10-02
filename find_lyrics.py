import requests as rq
from bs4 import BeautifulSoup as bs
# The song's name
song = ""
# Making the parameters for the url
params = {"q": song.lower()}
# Making a get request to the azlyric's search ulr + passing the above parameters to it
azlyrics_search = rq.get("https://search.azlyrics.com/search.php", params=params)
soup_1 = bs(azlyrics_search.text, "lxml")
# Get a list with all the results for the specific search
search_results = soup_1.find_all("table", {"class": "table table-condensed"})[-1].find_all("td", {"class": "text-left visitedlyr"})
# Take the first result from the search as the url with the lyrics on it
lyrics_url = search_results[0].a.get("href")
lyrics_page = rq.get(lyrics_url)
soup_2 = bs(lyrics_page.text, "lxml")
# Find the lyrics
lyrics = soup_2.find("div", {"class": "col-xs-12 col-lg-8 text-center"}).find_all("div")[6].get_text()
# Make a list with every line of the lyrics as a element and remove the first 2 because are html notes
lines = lyrics.splitlines()[2:]
processed_lyrics = ""
# Add a new line after every element and add it to a string
for line in lines:
	# This is for preventing it to add a new line to the end of the last line
	# Its not necessary but it looks nicer to me, to not have a extra line in the end of the lyrics
	if not line == lines[-1]:
		processed_lyrics += line + "\n"
	else:
		processed_lyrics += line
# Print the lyrics
print(processed_lyrics)
