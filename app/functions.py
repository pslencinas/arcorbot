

def formBienvenidaBot(token, name, personalEmail):
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": 
        {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Tlogic Arcor BOT - Reservas",
                                "weight": "Bolder",
                                "color": "Light",
                                "size": "Large"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "Hola **{}**".format(name),
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Aquí estoy para ayudarte desde Webex Teams Arcor.",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Qué es lo que desea hacer?",
                "wrap": True
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.Submit",
                                        "title": "Reservar Espacio de trabajo",
                                        "data": {
                                            "Token": token,
                                            "personalEmail": personalEmail,
                                            "Submit": "Reservar Espacio de trabajo"
                                        }
                                    }
                                ],
                                "spacing": "None"
                            }
                        ],
                        "width": "stretch"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.Submit",
                                        "title": "Reservar Cochera",
                                        "data": {
                                            "Token": token,
                                            "personalEmail": personalEmail,
                                            "Submit": "Reservar Cochera"
                                        }
                                    }
                                ],
                                "spacing": "None"
                            }
                        ],
                        "width": "stretch"
                    }
                ],
                "spacing": "None"
            },
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "ActionSet",
                                "actions": [
                                    {
                                        "type": "Action.Submit",
                                        "title": "Consultar Reservas",
                                        "data": {
                                            "Token": token,
                                            "personalEmail": personalEmail,
                                            "Submit": "Consultar Reservas"
                                        }
                                    }
                                ],
                                "spacing": "None"
                            }
                        ],
                        "width": "stretch"
                    }                    
                ],
                "spacing": "None"
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
		}
    }
    return attachment


def formReservas(token, sites, horario, personalEmail, date_now, five_dates):
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Seleccionar opciones",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "Edificio",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectSites",
                "choices": sites,
                "style": "compact"
            },
            {
                "type": "TextBlock",
                "text": "Fecha",
                "wrap": True
            },
            {
                "type": "Input.Date",
                "id": "inputDate",
                "value": date_now,
                "max": five_dates
            },
            {
                "type": "TextBlock",
                "text": "Horario",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectTimes",
                "choices": horario,
                "style": "compact"
            }
           
        ],
        "actions": [
            {
            "type": "Action.Submit",
            "title": "Buscar",
            "data": {
                "Token": token,
                "personalEmail": personalEmail,
                "Submit": "buscarWorkspace"
            }
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment


def formBuscarLoation(token, site_name, time, duration, date, locations, personalEmail, inputs):

    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Continuar con la reserva:",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "**Edificio:** " + site_name,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Fecha:** " + date,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Horario:** " + time,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Duración:** " + duration,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Seleccionar Sector",
                "size": "Medium",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectLocation",
                "choices": locations,
                "style": "compact"
            }
        ],
        "actions": [
            {
            "type": "Action.Submit",
            "title": "Buscar",
            "data": {
                "Token": token,
                "personalEmail": personalEmail,
                "Submit": "buscarWorkspace",
                "inputs": inputs
                }
            },
            {
            "type": "Action.Submit",
            "title": "Reiniciar reserva",
            "data": {
                "Token": token,
                "personalEmail": personalEmail,
                "Submit": "Reservar Espacio de trabajo"
            }
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment


def formBuscarWorkspace(token, site_name, horario, date, workspaces, personalEmail, inputs):
    
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Continuar con la reserva:",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "**Edificio:** " + site_name,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Fecha:** " + date,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Horario:** " + horario,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Espacios de trabajos disponibles",
                "size": "Medium",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectWorkspace",
                "choices": workspaces,
                "style": "compact"
            }
        ],
        "actions": [
            {
            "type": "Action.Submit",
            "title": "Confirmar Reserva",
            "data": {
                "Token": token,
                "personalEmail": personalEmail,
                "Submit": "confirmarWorkspace",
                "inputs": inputs
                }
            },
            {
            "type": "Action.Submit",
            "title": "Reiniciar reserva",
            "data": {
                "Token": token,
                "personalEmail": personalEmail,
                "Submit": "Reservar Espacio de trabajo"
            }
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment



def formConfirmWorkspace(token, item):
    
    hora_inicio = '%02d:00'%(int(item.hora_inicio))+'hs'
    hora_fin = '%02d:00'%(int(item.hora_fin))+'hs'

    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Reserva Confirmada",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "**Edificio:** " + item.workspace.site.name,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Fecha:** " + str(item.date),
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Horario:** {} a {}".format(hora_inicio, hora_fin),
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Espacio de trabajo asignado:** " + item.workspace.name,
                "wrap": True
            }
           
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Volver al Menu",
                "data": {
                    "Token": token,
                    "personalEmail": item.employee,
                    "Submit": "menu"
                }
            }
           
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment


def formConsultarWorkspace(token, items):
    
    body = []
    body.append(
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "Image",
                            "style": "Default",
                            "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                            "size": "Medium",
                            "height": "35px"
                        }
                    ],
                    "width": "auto"
                },
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "TextBlock",
                            "weight": "Bolder",
                            "text": "Reservas Confirmadas",
                            "horizontalAlignment": "Left",
                            "wrap": True,
                            "color": "Light",
                            "size": "Large",
                            "spacing": "Small"
                        }
                    ],
                    "width": "stretch"
                }
            ]
        }
    )

    if items:

        
        for item in items:
            personalEmail = item.employee
            hora_inicio = '%02d:00'%(int(item.hora_inicio))+'hs'
            hora_fin = '%02d:00'%(int(item.hora_fin))+'hs'

            if item.tipo == 'workspace':
                body.append(
                    {
                        "type": "TextBlock",
                        "text": "**Espacio de trabajo:** {}, {}".format(
                            item.workspace.name, item.workspace.site.name),
                        "wrap": True
                    }
                )
            else:
                body.append(
                    {
                        "type": "TextBlock",
                        "text": "**Cochera:** {}, {}".format(
                            item.cochera.name, item.cochera.site.name),
                        "wrap": True
                    }
                )
            body.append(
                {
                    "type": "TextBlock",
                    "text": "**Fecha:** {} de {} a {}".format(str(item.date), hora_inicio, hora_fin),
                    "wrap": True
                }
            )
            body.append(
                {
                    "type": "TextBlock",
                    "text": "",
                    "wrap": True
                }
            )
    
    else:
        personalEmail = ""
        body.append(
                {
                    "type": "TextBlock",
                    "text": "**No tiene Reservas agendadas**",
                    "wrap": True
                }
            )

      
    if items:
        attachment = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "body": body,
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "Cancelar Reserva",
                        "data": {
                            "Token": token,
                            "personalEmail": personalEmail,
                            "Submit": "cancelarReserva"
                        }
                    },
                    {
                        "type": "Action.Submit",
                        "title": "Volver al Menu",
                        "data": {
                            "Token": token,
                            "personalEmail": personalEmail,
                            "Submit": "menu"
                        }
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2"
            }
        }
    else:
        attachment = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "body": body,
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "Volver al Menu",
                        "data": {
                            "Token": token,
                            "personalEmail": personalEmail,
                            "Submit": "menu"
                        }
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2"
            }
        }




    return attachment


def formCocheras(token, sites, horario, personalEmail, date_now, five_dates):
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Seleccionar opciones",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "Edificio",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectSites",
                "choices": sites,
                "style": "compact"
            },
            {
                "type": "TextBlock",
                "text": "Fecha",
                "wrap": True
            },
            {
                "type": "Input.Date",
                "id": "inputDate",
                "value": date_now,
                "max": five_dates
            },
            {
                "type": "TextBlock",
                "text": "Horario",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectTimes",
                "choices": horario,
                "style": "compact"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Buscar",
                "data": {
                    "Token": token,
                    "personalEmail": personalEmail,
                    "Submit": "buscarCochera"
                }
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment


def formBuscarCocheras(token, site_name, horario, date, cocheras, personalEmail, inputs):

    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Continuar con la reserva:",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "**Edificio:** " + site_name,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Fecha:** " + date,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Horario:** " + horario,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Seleccionar Cochera",
                "size": "Medium",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectCocheras",
                "choices": cocheras,
                "style": "compact"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Confirmar",
                "data": {
                    "Token": token,
                    "personalEmail": personalEmail,
                    "Submit": "confirmarCochera",
                    "inputs": inputs
                    }
            },
            {
                "type": "Action.Submit",
                "title": "Reiniciar reserva",
                "data": {
                    "Token": token,
                    "personalEmail": personalEmail,
                    "Submit": "Reservar Espacio de trabajo"
                }
            },
            {
                "type": "Action.Submit",
                "title": "Volver al Menu",
                "data": {
                    "Token": token,
                    "personalEmail": personalEmail,
                    "Submit": "menu"
                }
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment



def formConfirmCochera(token, item):
    
    hora_inicio = '%02d:00'%(int(item.hora_inicio))+'hs'
    hora_fin = '%02d:00'%(int(item.hora_fin))+'hs'

    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Reserva Confirmada",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "**Edificio:** " + item.cochera.site.name,
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Fecha:** " + str(item.date),
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Horario:** {} a {}".format(hora_inicio, hora_fin),
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "**Cochera asignada:** " + item.cochera.name,
                "wrap": True
            }
           
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Volver al Menu",
                "data": {
                    "Token": token,
                    "personalEmail": item.employee,
                    "Submit": "menu"
                }
            }
           
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment


def formCancelarReserva(token, values, personalEmail):
    
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Cancelar Reserva:",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "Seleccionar Reserva a cancelar",
                "size": "Medium",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "SelectReserva",
                "choices": values,
                "style": "compact"
            }
        ],
        "actions": [
            {
            "type": "Action.Submit",
            "title": "Confirmar",
            "data": {
                "Token": token,
                "personalEmail": personalEmail,
                "Submit": "confirmarCancelacion"
                }
            },
            {
                "type": "Action.Submit",
                "title": "Volver al Menu",
                "data": {
                    "Token": token,
                    "personalEmail": personalEmail,
                    "Submit": "menu"
                }
            }
           
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment


def formConfirmarCancelacion(token, personalEmail):
    
    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "style": "Default",
                                "url": "https://testing.tsm.tlogic.com.ar/static/images/public/t-logo.png",
                                "size": "Medium",
                                "height": "35px"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": "Confirmación de Cancelación",
                                "horizontalAlignment": "Left",
                                "wrap": True,
                                "color": "Light",
                                "size": "Large",
                                "spacing": "Small"
                            }
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": "TextBlock",
                "text": "**Cancelación confirmada !!!** ",
                "wrap": True
            }           
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Volver al Menu",
                "data": {
                    "Token": token,
                    "personalEmail": personalEmail,
                    "Submit": "menu"
                }
            }
           
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2"
    }
    }
    return attachment
