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

from reloaded import Reloaded
from utils import *
from dao_m2o import add_reloaded_track, find_all_shows


url = 'http://www.m2o.it/special/real-trust-reloaded/'
url_reloaded = "http://www.m2o.it/reloaded/"
relative_path_music = "./M2Os/"
thread_number = 4


# old, now use reloaded module
class Episode(object):
    def __init__(self, name, page, link=""):
        self.name = name
        self.page = page
        self.link = link

    def __str__(self):
        return str(self.name) + " -- " + str(self.link)

# old, now use finder module
def get_first_player_link(url, url_reloaded):
    # standard page, in here we can always find the last track player link
    page_string, page = get_page(url)

    #for link in page.xpath("//a"):
    #    print "Name", link.text, "URL", link.get("href")

    # last track player link is inside an iframe (i don't like at all... but they use iframe)
    iframe_link = page.get_element_by_id("container").cssselect("iframe")[0].attrib['src']
    print "found first stream at: " + str(iframe_link) + "..."
    return iframe_link

def get_episode_list(player_page, cur_idShow):

    # open last track player page, it's just a page where i have a player and the list
    first_player_page_string, first_player_page = get_page(player_page)


    # now i find the real link list
    list_html = first_player_page.get_element_by_id("scrollbar1").find_class("overview")
    episode_list = []

    for link in list_html[0].xpath("//a"):
        track_link = link.get("href").encode('utf-8')
        #get idaudio
        idAudio = get_idAudio_from_url(track_link)
        #get idshow
        idShow = get_idShow_from_url(track_link)
        name = link.text.encode('utf-8')
        if(idShow != int(cur_idShow)):
            print "idshow mismatch... expected:" + str(cur_idShow)+",taken:"+str(idShow)+",on page:"+track_link+",from:"+player_page

        episode_list.append(Reloaded(name=name, idAudio=idAudio, idShow=idShow))
    print "I found " + str(len(episode_list)) + " tracks, downloading details..."

    # TODO: do it in parallel
    for episode_page in episode_list:
        track_string, track_page = get_page(build_player_page(m2o_reloaded_url,episode_page.idAudio, episode_page.idShow))

        music_link = track_page.cssselect("audio")[0].attrib['src']
        episode_page.linkFile = music_link
        try:
            add_reloaded_track(episode_page)
        except sqlalchemy.exc.IntegrityError as e:
            print "integrity for " + str(music_link) + " with id " + str(episode_page.idAudio)
        except Exception as e:
            print e.text
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

if __name__ == "__main__":
    print "Mumble mumble... searching for Real Trust on " + url

    mylsit =  find_all_shows()
    for obj in mylsit:
        print obj.idShow
        
    print "a " + 2

    episode_list = get_episode_list(player_page)
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
