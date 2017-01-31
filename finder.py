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

if __name__ == "__main__":
    max_idaudio = 50000
    max_thread = 100
    min_audio = 10000
    page = "http://www.m2o.it/reloaded/index.php?idaudio="

    from reloaded import Shows

    sh = Shows(idShow = 1, nameShow = "yuppie")
    from dao_m2o import add_show
    add_show(sh)

    print "1" + 1


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
