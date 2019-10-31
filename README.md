### This is a program I made for finding the lyrics of a song based on AZLyrics

---

* It will search on **AZLyrics** for a specific song and print the **lyrics** for the top result based on the given song's name.

* For more info about how it works you can see find_lyrics.py.

---

You can either run it from **Command Prompt**

```
py find_lyrics.py
```

* See more [here](example.md "example.md")

Or import it and use it as a **library**

```python
from find_lyrics import find_lyrics
song = "Numb"
lyrics, search_time = find_lyrics(song)
```

**NOTE:** The searching may take a while since the site's type is dynamic and the lyrics are loading after the main page does.

Feel free to use it **:)**
