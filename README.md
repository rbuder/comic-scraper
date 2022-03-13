# Algorithm

1. Config file should specify link to first comic page, html/div keyword to look for
2. We download the first page
3. Grep the comic
4. Get the "next" link
5. Repeat with #2 until no more "next" or "next" == "current"

# Config

Define a dict like so:
```
comics = {
  "xkcd" : {
    "first": "https://xkcd.com/1/",
    "div": "comic",
    "tag": "img"
  }
}
```