import urllib
# this tool is a parser for xml and html
from lxml import html

def get_page(url):
    page_string = urllib.urlopen(url).read()
    page = html.fromstring(page_string)
    return page_string, page

def get_idShow_from_url(url):
    return int(url[url.find("id=")+3:])

def get_idAudio_from_url(url):
    return int(url[url.find("idAudio=")+8:])

def build_player_page(m2o_reloaded_url, idAudio, idShow=""):
    return m2o_reloaded_url+"index.php?id="+str(idShow)+"&idaudio="+str(idAudio)

def get_folderShow_from_link(url):
    overName = url[url.find("reloaded/")+len("reloaded/"):]
    folder = overName[:overName.find("/")]

    return folder
