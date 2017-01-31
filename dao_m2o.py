#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from reloaded import Reloaded, Shows

dbname = "m2o.db"

def add_reloaded_track(track):
  eng = create_engine('sqlite:///+"dbname"+')

  Session = sessionmaker(bind=eng)
  ses = Session()

  ses.add(track)
  ses.commit()

def add_show(show):
  eng = create_engine('sqlite:///+"dbname"+')

  Session = sessionmaker(bind=eng)
  ses = Session()

  ses.add(show)
  ses.commit()
