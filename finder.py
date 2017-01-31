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
from dao_m2o import add_show
from reloaded import Show

settings = get_settings()

def thread_finder_shows(queue, pageurl_root):
    root_url = settings.get_m2o_reloaded_url()

def thread_finder(index, max_thread, max_idaudio, pageurl, min_audio):
    i = index + min_audio
    while i <= max_idaudio:
        pagestring, page = get_page(pageurl + str(i))
        title = str(page.find(".//h3").text.encode('utf-8'))

        if "Real Trust" in title:
            print str(i) + "-- " + title
        else:
            print str(i)


        i += index + max_thread

def get_all_href_of_a_in_container(page_url):
    rootpage_string, rootpage = get_page(page_url)

    a_list_categories= rootpage.get_element_by_id("container").cssselect("a")
    url_category_list =[]

    for a in a_list_categories:
        real_link = a.get("href").encode('utf-8')
        url_category_list.append(real_link)
    return url_category_list

def get_all_href_of_a_in_scrollbar(page_url):
    rootpage_string, rootpage = get_page(page_url)

    a_list_categories= rootpage.get_element_by_id("scrollbar1").cssselect("a")
    url_category_list =[]

    for a in a_list_categories:
        real_link = a.get("href").encode('utf-8')
        url_category_list.append(real_link)
    return url_category_list

def get_categories_url_list():
    root_url = settings.get_m2o_reloaded_url()
    return get_all_href_of_a_in_container(root_url)

def get_shows_from_category_page(url):
    return get_all_href_of_a_in_container(url)

def get_all_shows():
    shows_list = []
    url_category_list = get_categories_url_list()

    for category_url in url_category_list:
        shows_of_category=get_shows_from_category_page(category_url)
        shows_list.extend(shows_of_category)

    # add to db, unsafe
    import sqlalchemy
    for show_url in shows_list:
        try:
            add_show(get_info_on_show(show_url))
        except sqlalchemy.exc.IntegrityError:
            #usually there's already on db
            pass
        except Exception as e:
            print "not possible: " + show_url
    return shows_list

def get_info_on_show(url):
    showpage_string, showpage = get_page(url)

    show_page_php = showpage.get_element_by_id("container").cssselect("iframe")[0].attrib['src'].encode('utf-8')

    # isolate id
    idShow = int(show_page_php[show_page_php.find("id=")+3:])

    name = showpage.get_element_by_id("container").cssselect("iframe")[0]

    # published links, not all
    # alist = get_all_href_of_a_in_scrollbar(show_page_php)

    # remove :
    nameShow = showpage.cssselect("strong")[0].text[:-1].encode('utf-8')
    if nameShow[0] == " ":
        nameShow = nameShow[1:]

    show = Show(nameShow=nameShow, idShow=idShow, pageShow=url)

    return show






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
