#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from reloaded import Reloaded, Show
from PySettings.SettingsManager import SettingsManager


def get_engine():
    settings = SettingsManager.getSettings()
    db_name = settings.get_dbname()
    db_engine = settings.get_db_engine()
    db_user = settings.get_db_user()
    db_password = settings.get_db_password()
    db_ip = settings.get_db_ip()
    # to build database, execute this file

    #Not secure!!! warning injection!
    engine = create_engine(db_engine+'://'+db_user+':'+db_password+'@'+db_ip+'/'+db_name)

    return engine;


def add_reloaded_track(track):
  dbname = SettingsManager.getSettings().get_dbname()
  eng = get_engine()
  Session = sessionmaker(bind=eng)
  ses = Session()

  ses.add(track)
  ses.commit()

def add_show(show):
  dbname = SettingsManager.getSettings().get_dbname()
  eng = get_engine()

  Session = sessionmaker(bind=eng)
  ses = Session()

  ses.add(show)
  ses.commit()

def find_show_by_folderShow(folder):
    dbname = SettingsManager.getSettings().get_dbname()
    eng = get_engine()
    Session = sessionmaker(bind=eng)
    ses = Session()

    return  ses.query(Show).filter(Show.folderShow.like(folder))

def find_all_shows():
    dbname = SettingsManager.getSettings().get_dbname()
    eng =get_engine()
    Session = sessionmaker(bind=eng)
    ses = Session()

    return  ses.query(Show)
