url = 'http://www.m2o.it/special/real-trust-reloaded/'
print "Mumble mumble... searching for Real Trust on " + url


import urllib
from lxml import html


page = html.fromstring(urllib.urlopen(url).read())

for link in page.xpath("//a"):
    print "Name", link.text, "URL", link.get("href")
