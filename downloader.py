
def get_page(url):
    page_string = urllib.urlopen(url).read()
    page = html.fromstring(page_string)
    return page_string, page


url = 'http://www.m2o.it/special/real-trust-reloaded/'
print "Mumble mumble... searching for Real Trust on " + url

# this tool is for web requests
import urllib
# this tool is a parser for xml and html
from lxml import html

# standard page, in here we can always find the last track player link
page_string, page = get_page(url)

#for link in page.xpath("//a"):
#    print "Name", link.text, "URL", link.get("href")

# last track player link is inside an iframe (i don't like at all... but they use iframe)
iframe_link = page.cssselect("iframe")[0].attrib['src']
print "found first stream at: " + str(iframe_link) + "..."

# open last track player page, it's just a page where i have a player and the list
first_player_page_string, first_player_page = get_page(iframe_link)


# now i find the real link list
list_html = first_player_page.get_element_by_id("scrollbar1").find_class("overview")
player_link_list = []
for link in list_html[0].xpath("//a"):
    player_link_list.append((link.text, link.get("href")))
print "I found " + str(len(player_link_list)) + " tracks"
