import urllib2
import inspect
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from bs4 import BeautifulSoup

url = urllib2.urlopen("http://www.fly4free.com/flight-deals/belgium/").read()

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attrs

    # def handle_endtag(self, tag):
    #     print "End tag  :", tag

   ##   def handle_data(self, data):
    #     print "Data     :", data

   ##   def handle_comment(self, data):
    #     print "Comment  :", data


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
utf = url.decode('utf-8','ignore')
parser.feed(utf)