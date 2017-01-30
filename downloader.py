#!/usr/bin/env python
# -*- coding: utf-8 -*-
from file_util import *

# this is for file things
import os, sys
# this tool is for web requests
import urllib
# this tool is a parser for xml and html
from lxml import html
# for threads
from Queue import Queue
from threading import Thread


url = 'http://www.m2o.it/special/real-trust-reloaded/'
url_reloaded = "http://www.m2o.it/reloaded/"
relative_path_music = "./M2Os/"
thread_number = 4

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



def download_file(url, filename):
    loaded_file = urllib.urlopen(url)
    try:
        with open(filename,'wb') as output:
            output.write(loaded_file.read())
    except Exception as e:
        os.remove(filename)
        print str(e)
    finally:
        output.close()

def thread_downloader(queue):
    while not queue.empty():
        url, filename = queue.get()
        print "Downloading ..." + filename
        download_file(url, filename)
        queue.task_done()
        print "Downloaded " + filename

##
##
##
##


print "Mumble mumble... searching for Real Trust on " + url


episode_list = get_episode_list(url, url_reloaded)
# all we need is now in episode_list



try_to_create_folder(relative_path_music)

present_file_list = get_file_list_in_path(relative_path_music)

queue = Queue()

for track in episode_list:
    file_name = track.name + ".mp3"
    path_file = relative_path_music + file_name
    if not already_exists(path_file):
        queue.put((track.link, path_file))

for _ in range(thread_number):
    t = Thread(target=thread_downloader, args=[queue])
    t.daemon = True
    t.start()
try:
    queue.join()
except (KeyboardInterrupt, SystemExit):
    cleanup_stop_thread();
    sys.exit()
print "All done, bye! Tunz Tunz Tunz..."
