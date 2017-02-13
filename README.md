# M2ownloader
I really like Real Trust by DJ Molinaro... but M2O site doesn't allow directly to download traces....

This script is simply a python program that surfs on php site and find every m2o real trust mp3. 

This can be easily extended to all programs on M2O reloaded. 

## Need (Ubuntu)
* python (sudo apt install python-minimal)
* pip (sudo apt install python-pip)
* lxml (pip install lxml)
* sqlalchemy (pip install sqlalchemy)
* sqlite3 (apt install sqlite3)

## Installation
no installation required

## Usage
* initialize and load library with:
python control.py -init -load_info_shows -load_info_tracks

* watch current settings (saved in settings.txt) with
python control.py -settings

* read local library (you have to initialize it before, watch above)
python control.py -list shows
* watch all episodes of a series (example series with id 55)
python control.py -show 55

* download an episode 
python control.py -download_track 15002

* download all the show episodes
python control.py -download_show 55

## Updating
running -download_show and download_track doesn't overwrite your files.
To easily update local files with new ones of a show you have just to download_show again, downloaded tracks will be not touched.

I AM NOT RESPONSIBLE FOR ANY KIND OF USAGE OF THIS CODE. 
I AM NOT OWNER OF ANY RIGHTS FOR CONTENTS
I AM NOT RESPONSIBLE FOR ANY NOTE7 EXPLOSION (it could happen however...)
