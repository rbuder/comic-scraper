from bs4 import BeautifulSoup
from requests import get
import os

# Ctrl+Alt+Del
# they use a php API and Ajax, but there are also permalinks... back to bs4 :) 
# first comic: https://cad-comic.com/comic/nice-melon/

class Comic:
    __baseUrl = "https://cad-comic.com/"
    __page = None
    __soup = None

    def getPage(self, url):
        self.__page = get(url)

    def makeSoup(self):
        self.__soup = BeautifulSoup(self.__page.text, "html.parser")

    def getSrc(self):
        div = self.__soup.select("div.comicpage")
        img = div[0].select('img')
        return img[-1]

    def getNext(self):
        links = self.__soup.find_all("a")
        next = [link for link in links if link.get("rel") == ["next"]]
        return next[0].get("href")

    def getFirst(self):
        return self.getPage(f"{self.__baseUrl}/comic/nice-melon/")

    def downloadSource(self, src):
        res = get(src)
        filename = src.split("/")[-1]
        dir = f"./downloads/ctrlaltdel/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        filepath = f"{dir}/{filename}"
        with open(filepath, "wb") as f:
            f.write(res.content)

    def downloadAll(self):
        self.getFirst()
        self.makeSoup()
        next = self.getNext()
        nextUrl = next
        src = self.getSrc()
        self.downloadSource(src["src"])
        curUrl = ""
        while curUrl != nextUrl:
            self.getPage(nextUrl)
            self.makeSoup()
            next = self.getNext()
            src = self.getSrc()
            self.downloadSource(
                src["src"]
            )
            curUrl = nextUrl
            nextUrl = next
