from bottle import route, run, response, request, get, post, put, delete
import json

habitaciones = dict()


class Room:
    def __init__(self, idd, plazas, precio, ocupada, equipamiento):  #
        self.idd = idd
        self.plazas = plazas
        self.precio = precio
        self.ocupada = ocupada
        # [0]->armario [1]-> aire acondicionado [2]-> caja fuerte [3]-> escritorio [4]->wifi
        self.equipamiento = equipamiento

    def list_info(self):
        return "Habitacion: " + str(self.idd) + ", [Ocupada]:" + \
               str(self.ocupada) + ", plazas: " + str(self.plazas) + \
               "\nPrecio por noche:" + str(self.precio) + \
               "Equipamiento: " + str(self.equipamiento)


def database_to_json():
    datos = {'habitaciones': []}
    for key, room in habitaciones.items():
        datos['habitaciones'].append(
            {"idd": key,
             "plazas": room.plazas,
             "precio": room.precio,
             "ocupada": room.ocupada,
             "equipamiento": {
                 "armario": room.equipamiento[0],
                 "aire": room.equipamiento[1],
                 "caja": room.equipamiento[2],
                 "escritorio": room.equipamiento[3],
                 "wifi": room.equipamiento[4]
             }
             })
    return datos


def save_database():
    outfile = open('database.json', 'w')
    json.dump(database_to_json(), outfile)
    outfile.close()


def read_database():
    try:
        infile = open('database.json', "r")
    except FileNotFoundError:
        return
    datos = json.load(infile)
    for d in datos['habitaciones']:
        equip = []
        datos_equipo = d['equipamiento']
        equip.append(datos_equipo['armario'])
        equip.append(datos_equipo['aire'])
        equip.append(datos_equipo['caja'])
        equip.append(datos_equipo['escritorio'])
        equip.append(datos_equipo['wifi'])

        room = Room(d['idd'], d['plazas'], d['precio'], d['ocupada'], equip)
        habitaciones[room.idd] = room
        print("Añadida habitacion con idd:" + str(room.idd))


@post('/AddRoom')
def add_room():
    try:
        data = request.json
    except ValueError:
        print("Error al recibir los datos del cliente")
        return
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

    equip = [armario, ac, cajafuerte, escritorio, wifi]

    room = Room(max(habitaciones.keys()) + 1, plazas, precio, False, equip)

    habitaciones[room.idd] = room

    response.headers['Content-Type'] = 'application/json'

    respuesta = {'idd': room.idd, 'plazas': room.plazas, 'precio': room.precio}

    save_database()
    return json.dumps(respuesta)


@get('/ListRooms')
def list_rooms():
    to_return = []
    for key, room in habitaciones.items():
        to_return.append({"idd": key, "plazas": room.plazas, "precio": room.precio, "ocupada": room.ocupada,
                          "armario": room.equipamiento[0], "ac": room.equipamiento[1],
                          "cajafuerte": room.equipamiento[2], "escritorio": room.equipamiento[3],
                          "wifi": room.equipamiento[4]})
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(to_return)


@get('/ListRoomsOcup/<ocup>')
def list_rooms_ocup(ocup):
    to_return = []
    if int(ocup) == 1:
        bocup = True
    else:
        bocup = False

    for key, room in habitaciones.items():
        if room.ocupada == bocup:
            to_return.append({"idd": key, "plazas": room.plazas, "precio": room.precio, "ocupada": room.ocupada,
                              "armario": room.equipamiento[0], "ac": room.equipamiento[1],
                              "cajafuerte": room.equipamiento[2], "escritorio": room.equipamiento[3],
                              "wifi": room.equipamiento[4]})
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(to_return)


@get('/ListRoomIdd/<idd_hab>')
def list_room_idd(idd_hab):
    if int(idd_hab) not in habitaciones.keys():
        print("Error en el indice de la habitacion")
        return {}

    room = habitaciones[int(idd_hab)]
    respuesta = {"idd": room.idd, "plazas": room.plazas, "precio": room.precio, "ocupada": room.ocupada,
                 "armario": room.equipamiento[0], "ac": room.equipamiento[1], "cajafuerte": room.equipamiento[2],
                 "escritorio": room.equipamiento[3], "wifi": room.equipamiento[4]}
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(respuesta)


# PUT para modificar habitacion
@put('/ModifyRoom/<idd_hab>')
def modify_room(idd_hab):
    if int(idd_hab) not in habitaciones.keys():
        print("Error en el indice de la habitacion")
        return {}

    r = habitaciones[int(idd_hab)]

    print("Habitacion modificada:" + str(idd_hab))
    try:
        data = request.json
    except ValueError:
        print("Error al recibir los datos")
        return {}
    if data is None:
        raise ValueError
    new_plazas = data.get('plazas')
    if new_plazas != 0:
        r.plazas = new_plazas
    new_precio = data.get('precio')
    if new_precio != 0:
        r.precio = new_precio
    ocupacion = data.get('ocupada')
    r.ocupada = ocupacion
    op = data.get('op')
    if op:
        armario = data.get('armario')
        ac = data.get('ac')
        cajafuerte = data.get('cajafuerte')
        escritorio = data.get('escritorio')
        wifi = data.get('wifi')
        equip = [armario, ac, cajafuerte, escritorio, wifi]
        r.equipamiento = equip

    response.headers['Content-Type'] = 'application/json'

    respuesta = {'idd': r.idd}
    save_database()
    return json.dumps(respuesta)


@delete('/DeleteRoom/<idd_hab>')
def delete_room(idd_hab):
    if int(idd_hab) not in habitaciones.keys():
        print("Error en el identificador de la habitacion")
        return {}

    habitaciones.pop(int(idd_hab))

    respuesta = {'idd': idd_hab}
    print(respuesta)
    save_database()
    return json.dumps(respuesta)


if __name__ == "__main__":
    read_database()
    run(host='localhost', port=8080, debug=True)
