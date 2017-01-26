url = 'http://www.m2o.it/special/real-trust-reloaded/'
print "Mumble mumble... searching for Real Trust on " + url


import urllib
from lxml import html

page_string = urllib.urlopen(url).read()
page = html.fromstring(page_string)

#for link in page.xpath("//a"):
#    print "Name", link.text, "URL", link.get("href")


iframe_link = page.cssselect("iframe")[0].attrib['src']
print "found first stream at: " + str(iframe_link) + "..."

first_player_page_string = urllib.urlopen(iframe_link).read()
first_player_page = html.fromstring(first_player_page_string)

#print first_player_page_string


list_html = first_player_page.get_element_by_id("scrollbar1").find_class("overview")
for link in list_html[0].xpath("//a"):
    print "Name", link.text, "URL", link.get("href")
