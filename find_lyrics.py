import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from time import time
def find_lyrics(song=None):
	try:
		if song == None:
			song = input("Enter song: ")

		print("\nSearching for \"%s\"...\n" % (song))
		t_bf = time()

		# Making the parameters for the url
		url_params = {"q": song.lower()}
		options = Options()
		options.add_argument("--headless")
		options.add_argument("--disable-extensions")
		options.add_argument("log-level=3")
		options.add_experimental_option("excludeSwitches", ["enable-logging"])

		# Getting the search url
		search_url = rq.get("https://search.azlyrics.com/search.php", params=url_params).url
		driver = webdriver.Chrome(options=options)

		# Making a get request to the azlyric's
		driver.get(search_url)
		azlyrics_search = driver.page_source
		driver.quit()
		soup = bs(azlyrics_search, "lxml")

		# Get a list with all the results for the specific search
		search_results = soup.find_all("table", {"class": "table table-condensed"})[-1].find_all("td", {"class": "text-left visitedlyr"})

		# Take the first result from the search as the url with the lyrics on it
		lyrics_url = search_results[0].a.get("href")
		lyrics_page = rq.get(lyrics_url)
		soup = bs(lyrics_page.text, "lxml")

		# Find the lyrics
		lyrics = soup.find("div", {"class": "col-xs-12 col-lg-8 text-center"}).find_all("div")[5].get_text()

		# Make a list with every line of the lyrics as a element and remove the first 2 because are html notes
		lines = lyrics.splitlines()[2:]
		processed_lyrics = "\n".join(lines)

		# Search time (in seconds)
		t_af = time()
		search_time = round(t_af - t_bf, 1)

		return processed_lyrics, search_time
	except:
		return "\"%s\" Not Found..." % (song)

if __name__ == "__main__":
	print(find_lyrics()[0])
