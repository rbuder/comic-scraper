# Algorithm

1. Config file should specify link to first comic page, html/div keyword to look for
2. We download the first page
3. Grep the comic
4. Get the "next" link
5. Repeat with #2 until no more "next" or "next" == "current"

# Config

Currently only runs interactively:
```
# virtualenv -p $(which python3) .env
# source .env/bin/activate
# pip install -r requirements.txt
# python
Python 3.10.2 (main, Jan 15 2022, 19:56:27) [GCC 11.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from dilbert import *
>>> comic = Comic()
>>> comic.downloadAll()

```