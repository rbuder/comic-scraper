# About

This isn't to steal anyone's hard work. This is rather inspired by userfriendly.org going dark recently. *sad panda face*
This is to keep a personal record of some of my favourite web comics.

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

# How to use

This is still a highly manual WIP.

```
# Build the docker image
./build.sh
# run it
./run.sh
/usr/src/app # python
Python 3.9.7 (default, Nov 24 2021, 21:15:59) 
[GCC 10.3.1 20211027] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from dilbert import *
>>> comic = Comic()
>>> comic.downloadAll()
```
