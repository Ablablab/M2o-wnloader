#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from Settings.SettingsManager import get_settings


dbname = get_settings().get_dbname()


Base = declarative_base()

class Shows(Base):
    __tablename__ = "Shows"


    idShow = Column(Integer, primary_key=True)
    nameShow = Column(String)
    pageShow = Column(String)

class Reloaded(Base):
    __tablename__ = "Reloaded"


    idAudio = Column(Integer, primary_key=True)
    date = Column(String)
    idSerie = Column(Integer)
    idShow = Column(Integer, ForeignKey("Shows.idShow"))
    linkFile = Column(String)
    name = Column(String)

engine = create_engine('sqlite:///'+dbname)
Base.metadata.create_all(engine)
