import urllib.request
import datetime
from bs4 import BeautifulSoup


def logline(mytext):
    print(datetime.datetime.now() + mytext)


def getpage(myurl):
    req = urllib.request.Request(str(myurl), None, {
        'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    response = urllib.request.urlopen(req).read()
    var = BeautifulSoup(response, 'html.parser')
    print(var.prettify())


if __name__ == "__main__":
    getpage('https://ddg.gg')
