print "Mumble mumble... searching for Real Trust"
import urllib

import re
pat = re.compile('<DT><a href="[^"]+">(.+?)</a>')

url = 'http://www.m2o.it/special/real-trust-reloaded/'
sock = urllib.urlopen(url)
li = pat.findall(sock.read())
sock.close()

print li
