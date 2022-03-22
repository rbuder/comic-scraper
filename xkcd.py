from bs4 import BeautifulSoup
from requests import get
import os

# XKCD


class Comic:
    __baseUrl = "https://xkcd.com"
    __page = None
    __soup = None

    def getPage(self, url):
        self.__page = get(url)

    def makeSoup(self):
        self.__soup = BeautifulSoup(self.__page.text, "html.parser")

    def getSrc(self):
        imgdiv = self.__soup.find(id="comic")
        dlsrc = imgdiv.find_all("img")[0]
        return dlsrc

    def getNext(self):
        links = self.__soup.find_all("a")
        next = [link for link in links if link.get("rel") == ["next"]]
        return next[0].get("href")

    def getFirst(self):
        return self.getPage(f"{self.__baseUrl}/1/")

    def downloadSource(self, src, number, title, alt):
        res = get(f"https:{src}")
        filename = src.split("/")[-1]
        file = f"{str(number).zfill(4)} - {filename}"
        dir = f"./downloads/xkcd/"
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
        self.downloadSource(src["src"], 1, src["title"], src["alt"])
        curUrl = ""
        while curUrl != nextUrl:
            self.getPage(nextUrl)
            self.makeSoup()
            next = self.getNext()
            try:
                src = self.getSrc()
                self.downloadSource(
                    src["src"], int(next.replace("/", "")), src["title"], src["alt"]
                )
            except Exception as e:
                print(e)
                pass
            curUrl = nextUrl
            nextUrl = f"{self.__baseUrl}{next}"
