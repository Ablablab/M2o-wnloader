#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

class Shows(declarative_base()):
    __tablename__ = "Shows"

    idShow = Column(Integer, primary_key=True)
    nameShow = Column(String)

class Reloaded(declarative_base()):
    __tablename__ = "Reloaded"

    idAudio = Column(Integer, primary_key=True)
    date = Column(Date)
    idSerie = Column(Integer)
    idShow = Column(Integer, ForeignKey("Shows.idShow"))
    linkFile = Column(String)
    name = Column(String)
