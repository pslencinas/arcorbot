from . import functions
from fastapi import FastAPI, Depends, HTTPException, Request, status
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session
#from schema import Site, Configuration
from . import models
from . import crud
from webexteamssdk import WebexTeamsAPI, ApiError
import json, uuid
import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#access_token = 'ZGZlY2JlZDEtZmQyZi00YzdmLWI5N2EtNDBlYTg5YTEzZWVmM2NlYjAyODktNWU2_PF84_0d577422-f7ee-453e-b09d-5bbe97cd69c7'

#Jun2 2025
access_token = 'NmYyNDI5Y2MtMWMxMS00YjVhLTg3MjAtZDkxMDNjZGYyNmNiMzUzZmY1N2MtMGU2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
#bot_id = 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2MyNTJiY2M2LWIyOTEtNDFiMy1iMWJhLTMzY2YzNjc2NDUyZA'

WEBEX_BOT_USERNAME = 'reservation.arcor@webex.bot'

TIME = []
def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# @app.post('/device/info')
# def save_device_info(info: DeviceInfo, db=Depends(db)):
#     object_in_db = crud.get_device_info(db, info.token)
#     if object_in_db:
#         raise HTTPException(400, detail= crud.error_message('This device info already exists'))
#     return crud.save_device_info(db,info)

# @app.get('/device/info/{token}')
# def get_device_info(token: str, db=Depends(db)):
#     info = crud.get_device_info(db,token)
#     if info:
#         return info
#     else:
#         raise HTTPException(404, crud.error_message('No device found for token {}'.format(token)))

# @app.get('/device/info')
# def get_all_device_info(db=Depends(db)):
#     return crud.get_device_info(db)

# @app.post('/configuration')
# def save_configuration(config: Configuration, db=Depends(db)):
#     # always maintain one config
#     crud.delete_nudges_configuration(db)
#     return crud.save_nudges_configuration(db, config)

# @app.get('/configuration')
# def get_configuration(db=Depends(db)):
#     config = crud.get_nudges_configuration(db)
#     if config:
#         return config
#     else:
#         raise HTTPException(404, crud.error_message('No configuration set'))


@app.post('/v1/arcor')
async def webhook_listener(request: Request, db=Depends(db)):
    api = WebexTeamsAPI(access_token = access_token)

    print("\ndentro del POST webexBot /v1/arcor")
    headers = request.headers
    body = await request.json()
    #print(type(body))
    #body = json.dumps(body)
    print('\nwebexBot :: HEADER >> ',headers)
    print('\nwebexBot :: BODY >> ',body)
    data_id = body["data"]["id"]
    room_id = body["data"]["roomId"]

    

    if body["resource"] == 'attachmentActions' and body["name"] == 'My Attachment Action Webhook':
        print("\n::::::::::::: dentro del resource attachmentActions")

        message = api.attachment_actions.get(data_id)
        message = message.to_dict()
        print("\n::::::::::: Mensaje dentro de attachmentActions: {}\n".format(message))
        #print('Type: '+ message['type'])
        #print('inputs Title: '+ message['inputs']['Title'])
        token = message['inputs']['Token']
        reportedBy = message['inputs']['personalEmail']
        
        submit = message['inputs']['Submit']
        print('Submit: {}'.format(submit))

        if submit == 'menu':
            
            sUUID_token = str(uuid.uuid1())

            attachment = functions.formBienvenidaBot(sUUID_token, reportedBy, reportedBy)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'
            response = json.dumps({'message': message})
            return response, 200


        if submit == 'Reservar Espacio de trabajo':
            print("\n:::::::::: dentro de Reservar Espacio de trabajo")
            
            #sites = [{"value": str(row.id), "title": str(row.name)} for row in crud.get_sites(db) ]
            sites = [{"value": "2", "title": "Ranelagh"}]
            #times = [{"value": str(i), "title": '%02d:00'%(i)+'hs'} for i in range(8,20) ]
            horario = [{"value": "1", "title": "Mañana (08hs - 13hs)"}, {"value": "2", "title": "Tarde (13hs - 18hs)"}, {"value": "3", "title": "Día Completo (08hs - 18hs)"}]
            #duration = [{"value": "1", "title": "1 Hora"}, {"value": "2", "title": "2 Horas"}, {"value": "3", "title": "3 Horas"}]
            sUUID_token = str(uuid.uuid1())

            now = datetime.datetime.now()
            date_now = now.strftime('%Y-%m-%d')

            five_dates = now + datetime.timedelta(days=5)
            five_dates = five_dates.strftime('%Y-%m-%d')

            attachment = functions.formReservas(sUUID_token, sites, horario, reportedBy, date_now, five_dates)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200

        if submit == 'buscarLocation':

            inputs = message['inputs']
            token = inputs['Token']
            selectSited_id = inputs['SelectSites']
            selectTimes_id = inputs['SelectTimes']
            inputDate = inputs['inputDate']
            selectDuration_id = inputs['SelectDuration']

            locations = [{"value": str(row.id), "title": str(row.name)} for row in crud.get_locations_by_siteid(db, selectSited_id) ]

            site = crud.get_site_by_id(db, selectSited_id)
            time = '%02d:00'%(int(selectTimes_id))+'hs'
            duration = '1 Hora' if selectDuration_id == '1' else selectDuration_id+' Horas'

            attachment = functions.formBuscarLoation(token, site.name, time, duration, inputDate, locations, reportedBy, inputs)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200

        if submit == 'buscarWorkspace':
    
            inputs = message['inputs']
            token = inputs['Token']
            selectSited_id = inputs['SelectSites']
            inputDate = inputs['inputDate']
            selectTimes_id = inputs['SelectTimes']
            #selectDuration_id = inputs['SelectDuration']
            #selectLocation_id = message['inputs']['SelectLocation']

            workspaces = [{"value": str(row.id), "title": str(row.name)} for row in crud.get_workspace_by_siteid(db, selectSited_id) ]

            site = crud.get_site_by_id(db, selectSited_id)
            
            horario = ''
            if selectTimes_id == '1':
                horario = 'Mañana (08hs - 13hs)'
            elif selectTimes_id == '2':
                horario = 'Tarde (13hs - 18hs)'
            elif selectTimes_id == '3':
                horario = 'Día Completo (08hs - 18hs)'


            attachment = functions.formBuscarWorkspace(token, site.name, horario, inputDate, workspaces, reportedBy, inputs)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200

        
        
        if submit == 'confirmarWorkspace':
    
            inputs = message['inputs']['inputs']
            token = inputs['Token']
            datePython = datetime.datetime.strptime(inputs['inputDate'], '%Y-%m-%d')
            selectTimes_id = inputs['SelectTimes']

            duration = 5
            if selectTimes_id == '1':
                hora_inicio = 8
                hora_fin = 13
            elif selectTimes_id == '2':
                hora_inicio = 13
                hora_fin = 18
            elif selectTimes_id == '3':
                hora_inicio = 8
                hora_fin = 18
                duration = 10

            item = {
                'employee': reportedBy,
                'date': datePython,
                'hora_inicio': hora_inicio,
                'hora_fin': hora_fin,
                'duration': duration,
                'status': 'active',
                'description': 'test',
                'workspace_id': int(message['inputs']['SelectWorkspace'])
            }

            print(item)

            confirmation =  crud.create_reserva_workspace(db, item)
            print(confirmation)
            attachment = functions.formConfirmWorkspace(token, confirmation)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200
            
        
        if submit == 'Consultar Reservas':
        
            items = crud.get_reservas_by_name(db, reportedBy)
            attachment = functions.formConsultarWorkspace(token, items)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200


        if submit == 'cancelarReserva':
            print("\n:::::::::: dentro de cancelar Reservas")

            items = crud.get_reservas_by_name(db, reportedBy)
            values = []
            for item in items:
                if item.tipo == 'workspace':
                    values.append(
                        {
                            "value": str(item.id), 
                            "title": str(item.workspace.name) + ", " + str(item.date) + ' ' + 
                                '%02d:00'%(item.hora_inicio)+'hs' + ', ' + str(item.workspace.site.name)
                        }
                    )
                else:
                    values.append(
                        {
                            "value": str(item.id), 
                            "title": str(item.cochera.name) + ", " + str(item.date) + ' ' + 
                                '%02d:00'%(item.hora_inicio)+'hs' + ', ' + str(item.cochera.site.name)
                        }
                    )


            attachment = functions.formCancelarReserva(token, values, reportedBy)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200


        if submit == 'confirmarCancelacion':
            
            sUUID_token = str(uuid.uuid1())
            reserva_id = message['inputs']['SelectReserva']
            crud.delete_reserva_by_id(db, reserva_id)

            attachment = functions.formConfirmarCancelacion(sUUID_token, reportedBy)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200


        ''' Sector de reservas de Cochera'''

        if submit == 'Reservar Cochera':
            
            print("\n:::::::::: dentro de Reservar Cochera")
            
            #sites = [{"value": str(row.id), "title": str(row.name)} for row in crud.get_sites(db) ]
            sites = [{"value": "1", "title": "Lumina"}]
            horario = [{"value": "1", "title": "Mañana (08hs - 13hs)"}, {"value": "2", "title": "Tarde (13hs - 18hs)"}, {"value": "3", "title": "Día Completo (08hs - 18hs)"}]
            
            #times = [{"value": str(i), "title": '%02d:00'%(i)+'hs'} for i in range(8,20) ]
            #duration = [{"value": "2", "title": "2 Horas"}, {"value": "5", "title": "5 Horas"}, {"value": "10", "title": "10 Horas"}]
            sUUID_token = str(uuid.uuid1())

            now = datetime.datetime.now()
            date_now = now.strftime('%Y-%m-%d')

            five_dates = now + datetime.timedelta(days=5)
            five_dates = five_dates.strftime('%Y-%m-%d')

            attachment = functions.formCocheras(sUUID_token, sites, horario, reportedBy, date_now, five_dates)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200


        if submit == 'buscarCochera':
    
            inputs = message['inputs']
            token = inputs['Token']
            selectSited_id = inputs['SelectSites']
            selectTimes_id = inputs['SelectTimes']
            inputDate = inputs['inputDate']
            #selectDuration_id = inputs['SelectDuration']

            cocheras = [{"value": str(row.id), "title": str(row.name)} for row in crud.get_cocheras_by_siteid(db, selectSited_id) ]

            horario = ''
            if selectTimes_id == '1':
                horario = 'Mañana (08hs - 13hs)'
            elif selectTimes_id == '2':
                horario = 'Tarde (13hs - 18hs)'
            elif selectTimes_id == '3':
                horario = 'Día Completo (08hs - 18hs)'

            site = crud.get_site_by_id(db, selectSited_id)
            
            attachment = functions.formBuscarCocheras(token, site.name, horario, inputDate, cocheras, reportedBy, inputs)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200


        if submit == 'confirmarCochera':
        
            inputs = message['inputs']['inputs']
            token = inputs['Token']
            datePython = datetime.datetime.strptime(inputs['inputDate'], '%Y-%m-%d')
            selectTimes_id = inputs['SelectTimes']

            duration = 5
            if selectTimes_id == '1':
                hora_inicio = 8
                hora_fin = 13
            elif selectTimes_id == '2':
                hora_inicio = 13
                hora_fin = 18
            elif selectTimes_id == '3':
                hora_inicio = 8
                hora_fin = 18
                duration = 10

            item = {
                'employee': reportedBy,
                'date': datePython,
                'hora_inicio': hora_inicio,
                'hora_fin': hora_fin,
                'duration': duration,
                'status': 'active',
                'description': 'test',
                'cochera_id': int(message['inputs']['SelectCocheras'])
            }

            print(item)

            confirmation =  crud.create_reserva_cochera(db, item)
            print(confirmation)
            attachment = functions.formConfirmCochera(token, confirmation)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200
        
   
    if body["resource"] == 'messages' and body["name"] == 'Arcor Webhook':

        personalEmail = body["data"]["personEmail"]
        print('\n:::::::::::::: Dentro del Menu Bienvenida: {}\n'.format(personalEmail))

        if personalEmail == WEBEX_BOT_USERNAME:
            message = api.messages.get(data_id)
            print('Mensaje: '+ message.text)
            message = 'OK'

            response = json.dumps({'message': message})
            return response, 200

        else:
            # msg = """
            #     Hola {}. Estos son los comandos que entiendo:
            #     1. Para reportar un Incidente escribir: **reportar incidente** 
            #     2. Para generar una Solicitud escribir: **generar solicitud**
            #     3. **ayuda**
            #     """.format(personalEmail)

            # api.messages.create(room_id, markdown="{}".format(msg))

            sUUID_token = str(uuid.uuid1())

            attachment = functions.formBienvenidaBot(sUUID_token, personalEmail, personalEmail)
            api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

            message = 'OK'
            response = json.dumps({'message': message})
            return response, 200

    

    #response = json.dump({'message': message})
    return 'OK'