from bottle import route, run, template, response, request, get, post, put, delete
import numpy as np
import json

contadorHabitaciones = 0

habitaciones = dict()


class Room():
    def __init__(self, idd, plazas, precio):  #
        self.idd = idd
        self.plazas = plazas
        self.precio = precio
        self.ocupacion = False
        self.dni_ocupante = ""
        self.telefono = 0
        # [0]->armario [1]-> aire acondicionado [2]-> caja fuerte [3]-> escritorio [4]->wifi
        self.equipamiento = np.random.randint(0, 2, 5)

    def listar_info(self):
        return "Habitacion: " + str(self.idd) + ", [Ocupada]:" + \
               str(self.ocupacion) + ", plazas: " + str(self.plazas) + \
               "\nPrecio por noche:" + str(self.precio) + \
               "La habitacion tiene: " + str(self.equipamiento)


@route('/pruebaget', method='GET')
def index():
    rv = "Hello World !"
    return dict(data=rv)


@route('/pruebapost', method='POST')
def prueba():
    try:
        data = request.json
    except:
        raise ValueError
    if data is None:
        raise ValueError
    name = data['name']
    rv = "Hello " + name + " !"
    return dict(data=rv)


@route('/pruebaput', method='PUT')
def pruebaput():
    try:
        data = request.json
    except:
        raise ValueError
    if data is None:
        raise ValueError
    name = data['name']
    rv = "Hello " + name + " !"

    return dict(data=rv)


@post('/PedirHabitacion')
def pedir_hab():
    global contadorHabitaciones
    data = request.json

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


#@request('/listaHabitaciones', method='REQUEST')
#def listarHab():
 #   for r in habitaciones:
  #      print(r.listarInfo())


if __name__ == "__main__":

    run(host='localhost', port=8080, debug=True)

    rooms = [10]
    for i in range(0, 9):
        r = Room(i, 4)
        print(r.listarInfo())
