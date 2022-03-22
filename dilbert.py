from bs4 import BeautifulSoup
from requests import get
import os

# dilbert
# first comic: https://dilbert.com/strip/1989-04-17
# <div class="img-comic-container"></div>

class Comic:
    __baseUrl = "https://dilbert.com"
    __page = None
    __soup = None

    def getPage(self, url):
        self.__page = get(url)

    def makeSoup(self):
        self.__soup = BeautifulSoup(self.__page.text, "html.parser")

    def getSrc(self):
        img = self.__soup.select("img.img-comic")
        return img[0]

    def getNext(self):
        links = self.__soup.select("a.js-load-comic-newer")
        return links[0].get("href")

    def getFirst(self):
        return self.getPage(f"{self.__baseUrl}/strip/1989-04-17")

    def downloadSource(self, src, date, alt):
        res = get(src)
        filename = src.split("/")[-1]
        file = f"{date}.gif"
        dir = f"./downloads/dilbert/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        filepath = f"{dir}/{file}"
        with open(filepath, "wb") as f:
            f.write(res.content)

    def downloadAll(self):
        self.getFirst()
        self.makeSoup()
        next = self.getNext()
        nextUrl = f"{self.__baseUrl}{next}"
        src = self.getSrc()
        self.downloadSource(src["src"], "1989-04-17", src["alt"])
        curUrl = ""
        while curUrl != nextUrl:
            self.getPage(nextUrl)
            self.makeSoup()
            next = self.getNext()
            src = self.getSrc()
            self.downloadSource(
                src["src"], next.split('/')[-1], src["alt"]
            )
            curUrl = nextUrl
            nextUrl = f"{self.__baseUrl}{next}"
