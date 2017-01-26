url = 'http://www.m2o.it/special/real-trust-reloaded/'
print "Mumble mumble... searching for Real Trust on " + url


import urllib
from lxml import html

page_string = urllib.urlopen(url).read()
page = html.fromstring(page_string)

#for link in page.xpath("//a"):
#    print "Name", link.text, "URL", link.get("href")

#print page_string

iframe_link = page.cssselect("iframe")[0].attrib['src']
print iframe_link

first_player_page_string = urllib.urlopen(iframe_link).read()
first_player_page = html.fromstring(first_player_page_string)

print first_player_page_string
print 1 + "a"

list_html = page.get_element_by_id("scrollbar1").find_class("overview")
for link in list_html.xpath("//a"):
    print "Name", link.text, "URL", link.get("href")
