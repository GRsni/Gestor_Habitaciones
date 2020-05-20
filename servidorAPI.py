from bottle import route, run, template, response, request, get, post, put
import json
import numpy as np

contadorHabitaciones = 1

habitaciones = dict()


class Room():
    def __init__(self, idd, plazas, precio,equipamiento):  #
        self.idd = idd
        self.plazas = plazas
        self.precio = precio
        self.ocupada = 0 #0: libre 1:ocupada
        # [0]->armario [1]-> aire acondicionado [2]-> caja fuerte [3]-> escritorio [4]->wifi
        self.equipamiento = equipamiento
    def listar_info(self):
        return "Habitacion: " + str(self.idd) + ", [Ocupada]:" + \
               str(self.ocupacion) + ", plazas: " + str(self.plazas) + \
               "\nPrecio por noche:" + str(self.precio) + \
               "Equipamiento: " + str(self.equipamiento)


@post('/AddRoom')
def pedir_hab():
    global contadorHabitaciones
    try:
        data = request.json
    except:
        raise ValueError
    if data is None:
        raise ValueError
    plazas = data.get('plazas')
    precio = data.get('precio')
    armario = data.get('armario')
    ac = data.get('ac')
    cajafuerte = data.get('cajafuerte')
    escritorio = data.get('escritorio')
    wifi = data.get('wifi')

    if plazas is None or precio is None or armario is None or ac is None or cajafuerte is None or escritorio is None or wifi is None:
        raise ValueError

    equip = []
    equip.append(armario)
    equip.append(ac)
    equip.append(cajafuerte)
    equip.append(escritorio)
    equip.append(wifi)

    room = Room(contadorHabitaciones, plazas, precio,equip)
    contadorHabitaciones += 1

    habitaciones[room.idd] = room

    response.headers['Content-Type'] = 'application/json'

    respuesta = {'idd': room.idd, 'plazas': room.plazas, 'precio': room.precio}

    return json.dumps(respuesta)


@get('/ListRooms')
def list_rooms():
    to_return = []
    for key, room in habitaciones.items():
        to_return.append({"idd": key, "plazas": room.plazas, "precio": room.precio, "ocupada": room.ocupada, "armario": room.equipamiento[0], "ac":room.equipamiento[1], "cajafuerte":room.equipamiento[2], "escritorio":room.equipamiento[3],"wifi":room.equipamiento[4]})
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(to_return)


@get('/ListRoomIdd/<idd_hab>')
def list_room_idd(idd_hab):
    room=habitaciones[int(idd_hab)]
    respuesta= {"idd": room.idd, "plazas": room.plazas, "precio": room.precio, "ocupada": room.ocupada, "armario": room.equipamiento[0], "ac":room.equipamiento[1], "cajafuerte":room.equipamiento[2], "escritorio":room.equipamiento[3],"wifi":room.equipamiento[4]}
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(respuesta)


# PUT para modificar habitacion
@put('/ModifyRoom/<idd_hab>')
def modify_room(idd_hab):
    r=habitaciones[int(idd_hab)]
    print(idd_hab)
    try:
        data = request.json
    except:
        raise ValueError
    if data is None:
        raise ValueError
    new_plazas=data.get('plazas')
    if new_plazas!=0:
        r.plazas=new_plazas
    new_precio=data.get('precio')
    if  new_precio!=0:
        r.precio=new_precio
    ocupacion=data.get('ocupada')
    r.ocupada=ocupacion
    op=data.get('op')
    if op==1:
        armario = data.get('armario')
        ac = data.get('ac')
        cajafuerte = data.get('cajafuerte')
        escritorio = data.get('escritorio')
        wifi = data.get('wifi')
        equip = []
        equip.append(armario)
        equip.append(ac)
        equip.append(cajafuerte)
        equip.append(escritorio)
        equip.append(wifi)
        r.equipamiento=equip

    response.headers['Content-Type'] = 'application/json'

    respuesta = {'idd': r.idd}
    print(respuesta)
    return json.dumps(respuesta)


# GET para habitacion concreta


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
