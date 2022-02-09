from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date
from .database import Base
from sqlalchemy import Column, String, Boolean, Integer


class Site(Base):
    __tablename__ = 'site'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    site_id = Column(Integer, ForeignKey('site.id', ondelete='CASCADE'))
    site = relationship(Site)
    

class Workspace(Base):
    __tablename__ = 'workspace'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    site_id = Column(Integer, ForeignKey('site.id', ondelete='CASCADE'))
    site = relationship(Site)


class Cochera(Base):
    __tablename__ = 'cochera'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    site_id = Column(Integer, ForeignKey('site.id', ondelete='CASCADE'))
    site = relationship(Site)


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key = True, autoincrement = True)
    employee = Column(String)
    date = Column(Date)
    hora_inicio = Column(Integer)
    hora_fin = Column(Integer)
    duration = Column(Integer)
    status = Column(String)
    description = Column(String)
    workspace_id = Column(Integer, ForeignKey('workspace.id', ondelete='CASCADE'))
    workspace = relationship(Workspace)
    cochera_id = Column(Integer, ForeignKey('cochera.id', ondelete='CASCADE'))
    cochera = relationship(Cochera)
    tipo = Column(String)


