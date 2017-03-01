from reloaded import init_db
from finder import add_all_shows, get_all_tracks
import argparse
from PySettings import SettingsManager

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple tool to download m2o tracks from website. To begin, you have to create a local db with -init. After that you can download shows and track info with -load_info_shows and -load_info_tracks (needed).')
    parser.add_argument('-settings', help='Show local configuration', required=False, default=False, action="store_true")
    parser.add_argument('-init', help='Create a local sqlite db', required=False, default=False, action="store_true")
    parser.add_argument('-load_info_shows', help='Download and update list of shows', required=False,default=False, action="store_true")
    parser.add_argument('-load_info_tracks', help='Download and update list of tracks (episodes)', required=False,default=False, action="store_true")

    opts = parser.parse_args()

    if opts.settings:
        print str(SettingsManager.getSettings())
    if opts.init:
        print "Initializing db sqlite"
        init_db()
        print "Initialized"
    if opts.load_info_shows:
        print "Loading shows info on db(this can take a while)"
        add_all_shows()
        print "Done"
    if opts.load_info_tracks:
        print "Loading tracks info on db(this can take a while, cannot be interrupted)"
        get_all_tracks()
        print "Done"
