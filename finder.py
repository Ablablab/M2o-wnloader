#!/usr/bin/env python
# -*- coding: utf-8 -*-
from downloader import *

# this is for file things
import os, sys
# this tool is for web requests
import urllib
# this tool is a parser for xml and html
from lxml import html
# for threads
from Queue import Queue
from threading import Thread
from Settings.SettingsManager import get_settings

settings = get_settings()

def thread_finder_shows(queue, pageurl_root):
    root_url = settings.get_m2o_reloaded_url()

def thread_finder(index, max_thread, max_idaudio, pageurl, min_audio):
    i = index + min_audio
    while i <= max_idaudio:
        pagestring, page = get_page(pageurl + str(i))
        title = str(page.find(".//h3").text)

        if "Real Trust" in title:
            print str(i) + "-- " + title
        else:
            print str(i)


        i += index + max_thread

def get_all_shows():
    root_url = settings.get_m2o_reloaded_url()

    rootpage_string, rootpage = get_page(root_url)



def get_all_tracks():
    max_idaudio = settings.get_max_idaudio()
    max_thread = settings.get_threads_number()
    min_audio = settings.get_min_idaudio()
    page = "http://www.m2o.it/reloaded/index.php?idaudio="

    #from reloaded import Shows
    #sh = Shows(idShow = 1, nameShow = "yuppie")
    #from dao_m2o import add_show
    #add_show(sh)


    print "creating threads"
    threads = []
    for thread in range(max_thread):
        t = Thread(target=thread_finder, args=[thread, max_thread, max_idaudio, page, min_audio])
        t.daemon = True
        t.start()
        threads.append(t)

    print "waiting for threads' job"
    for thread in threads:
        thread.join()
    print "done, bye"

if __name__ == "__main__":
    get_all_shows()
