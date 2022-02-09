from datetime import date
from pydantic import BaseModel
from typing import Optional

class Site(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Location(BaseModel):
    name: str
    site_id: int
   
    class Config:
        orm_mode = True


class Workspace(BaseModel):
    name: str
    location_id: int
   
    class Config:
        orm_mode = True

class Cochera(BaseModel):
    name: str
    site_id: int
   
    class Config:
        orm_mode = True

class Reservation(BaseModel):
    employee: str
    date: date
    hora_inicio = int
    hora_fin = int
    status = str
    description = str
    workspace_id = int
    cochera_id = int
    tipo = str
    
    class Config:
        orm_mode = True