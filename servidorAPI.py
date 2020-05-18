from bottle import route, run, template,response,request,get,post,put
import json
import numpy as np

contadorHabitaciones = 0

habitaciones = dict()

class Room():
    def __init__(self, idd, plazas, precio):  #
        self.idd = idd
        self.plazas = plazas
        self.precio = precio
        self.ocupacion = False
        # [0]->armario [1]-> aire acondicionado [2]-> caja fuerte [3]-> escritorio [4]->wifi
        self.equipamiento = np.random.randint(0, 2, 5)

    def listar_info(self):
        return "Habitacion: " + str(self.idd) + ", [Ocupada]:" + \
               str(self.ocupacion) + ", plazas: " + str(self.plazas) + \
               "\nPrecio por noche:" + str(self.precio) + \
               "La habitacion tiene: " + str(self.equipamiento)



@post('/PedirHabitacion')
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

    if plazas is None or precio is None:
        raise ValueError

    room = Room(contadorHabitaciones, plazas, precio)
    contadorHabitaciones += 1

    habitaciones[room.idd] = room

    response.headers['Content-Type'] = 'application/json'

    respuesta = {'idd': room.idd, 'plazas': room.plazas, 'precio': room.precio}

    return json.dumps(respuesta)

@get('/ListRooms')
def list_rooms():
    to_return=[]
    for key, value in habitaciones.items():
        to_return.append({"idd":key, "plazas":value.plazas , "precio":value.precio})

    response.headers['Content-Type'] = 'application/json'
    return json.dumps(to_return)



if __name__ == "__main__":

    run(host='localhost', port=8080, debug=True)