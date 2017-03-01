    #!/usr/bin/python
    # -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from PySettings import SettingsManager



Base = declarative_base()
class Show(Base):

    __tablename__ = "Show"


    idShow = Column(Integer, primary_key=True)
    nameShow = Column(String)
    pageShow = Column(String)
    folderShow = Column(String, unique=True)

class Reloaded(Base):
    __tablename__ = "Reloaded"


    idAudio = Column(Integer, primary_key=True)
    date = Column(String)
    idShow = Column(Integer, ForeignKey("Show.idShow"))
    linkFile = Column(String)
    name = Column(String)

def get_engine():
    settings = SettingsManager.SettingsManager.getSettings()
    db_name = settings.get_dbname()
    db_engine = settings.get_db_engine()
    db_user = settings.get_db_user()
    db_password = settings.get_db_password()
    db_ip = settings.get_db_ip()
    # to build database, execute this file

    #Not secure!!! warning injection!
    engine = create_engine(db_engine+'://'+db_user+':'+db_password+'@'+db_ip+'/'+db_name)

    return engine;

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
