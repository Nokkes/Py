import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("http://www.fly4free.com/flight-deals/belgium/").read()
soup = BeautifulSoup(url, 'html.parser')

res = soup.find("div", { "class" : "entry" })