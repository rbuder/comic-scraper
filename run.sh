#!/bin/sh

docker run --rm -it -v "$(pwd)"/downloads:/usr/src/app/downloads comic-scraper sh
