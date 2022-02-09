from sqlalchemy.orm import Session
from . import schema, models


# def save_device_info(db: Session, info: schema.DeviceInfo):
#     device_info_model = models.DeviceInfo(**info.dict())
#     db.add(device_info_model)
#     db.commit()
#     db.refresh(device_info_model)
#     return device_info_model

# def get_device_info(db: Session, token: str = None):
#     if token is None:
#         return db.query(models.DeviceInfo).all()
#     else:
#         return db.query(models.DeviceInfo).filter(models.DeviceInfo.token == token).first()

# def save_nudges_configuration(db: Session, config: schema.Configuration):
#     config_model = models.Configuration(**config.dict())
#     db.add(config_model)
#     db.commit()
#     db.refresh(config_model)
#     return config_model

# def get_nudges_configuration(db: Session):
#     return db.query(models.Configuration).first()

# def delete_nudges_configuration(db: Session):
#     db.query(models.Configuration).delete()

# def error_message(message):
#     return {
#         'error': message
#     }

def get_sites(db: Session):
    return db.query(models.Site).all()
    

def get_site_by_id(db: Session, id: int):
    return db.query(models.Site).filter(models.Site.id == id).first()

def get_location_by_id(db: Session, id: int):
    return db.query(models.Location).filter(models.Location.id == id).first()

def get_locations_by_siteid(db: Session, id: int):
    return db.query(models.Location).filter(models.Location.site_id == id).all()

def get_workspace_by_siteid(db: Session, id: int):
    return db.query(models.Workspace).filter(models.Workspace.site_id == id).all()

def create_reserva_workspace(db: Session, item: any):

    data = models.Reservation(
        employee= item['employee'],
        date= item['date'],
        hora_inicio= item['hora_inicio'],
        hora_fin= item['hora_fin'],
        duration= item['duration'],
        status= item['status'],
        description= item['description'],
        workspace_id= item['workspace_id'],
        tipo = 'workspace'
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_reservas_by_name(db: Session, name: str):
    return db.query(models.Reservation).filter(
        models.Reservation.employee == name).all()


def get_cocheras_by_siteid(db: Session, id: int):
    return db.query(models.Cochera).filter(models.Cochera.site_id == id).all()

def create_reserva_cochera(db: Session, item: any):
    
    data = models.Reservation(
        employee= item['employee'],
        date= item['date'],
        hora_inicio= item['hora_inicio'],
        hora_fin= item['hora_fin'],
        duration= item['duration'],
        status= item['status'],
        description= item['description'],
        cochera_id= item['cochera_id'],
        tipo = 'cochera'
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def delete_reserva_by_id(db: Session, id: int):
    item = db.query(models.Reservation).filter(models.Reservation.id == id).first()

    db.delete(item)
    db.commit()

    return