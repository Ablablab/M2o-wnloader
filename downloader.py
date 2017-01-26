#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this tool is for web requests
import urllib
# this tool is a parser for xml and html
from lxml import html

def get_page(url):
    page_string = urllib.urlopen(url).read()
    page = html.fromstring(page_string)
    return page_string, page

class Episode(object):
    def __init__(self, name, page, link=""):
        self.name = name
        self.page = page
        self.link = link

    def __str__(self):
        return str(self.name) + " -- " + str(self.link)

def get_episode_list(url, url_reloaded):

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
    episode_list = []

    for link in list_html[0].xpath("//a"):
        episode_list.append(Episode(link.text.encode('utf-8'), link.get("href").encode('utf-8')))
    print "I found " + str(len(episode_list)) + " tracks, downloading details..."

    # TODO: do it in parallel
    for episode_page in episode_list:
        track_string, track_page = get_page(url_reloaded + episode_page.page)

        music_link = track_page.cssselect("audio")[0].attrib['src']
        episode_page.link = music_link

    return episode_list

url = 'http://www.m2o.it/special/real-trust-reloaded/'
url_reloaded = "http://www.m2o.it/reloaded/"
print "Mumble mumble... searching for Real Trust on " + url


episode_list = get_episode_list(url, url_reloaded)
# all we need is now in episode_list

for episode in episode_list:
    print str(episode)
