import requests, json

urlBase = 'http://localhost:8080'

urlAdd = '/AddRoom'
urlListAll = '/ListRooms'
urlModify = '/ModifyRoom'
urlListIdd = '/ListRoomIdd'


def AddRoomMenu():
    print("Introduce las plazas de la habitacion:")
    plazas = int(input())
    print("Introduce el precio por noche:")
    precio = int(input())
    print("¿Tiene armario? (1=si 0=no)")
    arm = int(input())
    print("¿Tiene aire acondicionado? (1=si 0=no)")
    ac = int(input())
    print("¿Tiene caja fuerte? (1=si 0=no)")
    cf = int(input())
    print("¿Tiene escritorio? (1=si 0=no)")
    esc = int(input())
    print("¿Tiene wifi? (1=si 0=no)")
    wifi = int(input())
    AddRoom(plazas, precio, arm, ac, cf, esc, wifi)


def AddRoom(plazas, precio, armario, ac, cajafuerte, escritorio, wifi):
    # INSERTA 1 HABITACIÓN
    data2 = {'plazas': plazas, 'precio': precio, 'armario': armario, 'ac': ac, 'cajafuerte': cajafuerte,
             'escritorio': escritorio, 'wifi': wifi}
    headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r2 = requests.post(str(urlBase + urlAdd), data=json.dumps(data2), headers=headers2)
    d2 = r2.json()
    print("Id de habitacion insertada: " + str(d2['idd']))


def GetRoomStringFromJSON(data):
    out = 'idd: ' + str(data['idd']) + ' plazas: ' + str(data['plazas']) + ' precio: ' + \
          str(data['precio']) + ' € Ocupada: '
    if data['ocupada'] == 1:
        out += ' si '
    else:
        out += ' no'
    out += '\n EQUIPAMIENTO: \n'
    if data['armario'] == 1:
        out += '\t- armario \n'
    if data['ac'] == 1:
        out += '\t- aire acondicionado \n'
    if data['cajafuerte'] == 1:
        out += '\t- caja fuerte \n'
    if data['escritorio'] == 1:
        out += '\t- escritorio \n'
    if data['wifi'] == 1:
        out += '\t- wifi \n'
    return out


def ListRooms():
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListAll))
    d = response.json()
    for r in d:
        print(GetRoomStringFromJSON(r))


def ListRoomIdd(idd):
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListIdd + '/' + str(idd)))
    r = response.json()
    print(GetRoomStringFromJSON(r))


def ListRoomsOcupancy(ocup):
    response = requests.get(str(urlBase) + str(urlListAll))
    rooms = response.json()
    for r in rooms:
        if r['ocupada'] == ocup:
            print(GetRoomStringFromJSON(r))


def ModifyRoomMenu():
    arm = ac = cf = esc = wifi = 0
    print("Introduce el identificador de la habitacion a modificar:")
    idd = int(input())
    print("Introduzca nuevo nº de plazas (0 si no desea modificar)")
    plazas = int(input())
    print("Introduce nuevo precio por noche (0 si no desea modificar)")
    precio = int(input())
    print("¿Se encuentra ocupada actualmente? (1=si 0=no)")
    ocupada = int(input())
    print("¿Desea cambiar el equipamiento? (1=si 0=no)")
    op = int(input())
    if op == 1:
        print("¿Tiene armario? (1=si 0=no)")
        arm = int(input())
        print("¿Tiene aire acondicionado? (1=si 0=no)")
        ac = int(input())
        print("¿Tiene caja fuerte? (1=si 0=no)")
        cf = int(input())
        print("¿Tiene escritorio? (1=si 0=no)")
        esc = int(input())
        print("¿Tiene wifi? (1=si 0=no)")
        wifi = int(input())
    ModifyRoom(idd, plazas, precio, ocupada, op, arm, ac, cf, esc, wifi)


def ModifyRoom(idd, plazas, precio, ocupada, op, arm, ac, cf, esc, wifi):
    data = {'plazas': plazas, 'precio': precio, 'ocupada': ocupada, 'op': op, 'armario': arm, 'ac': ac,
            'cajafuerte': cf,
            'escritorio': esc, 'wifi': wifi}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.put(str(urlBase + urlModify + '/' + str(idd)), data=json.dumps(data), headers=headers)
    d = r.json()
    print("Id de habitacion modificada: " + str(d['idd']))


if __name__ == "__main__":
    while True:
        print("\nElije la operación a realizar:\n- [0] Listar todas las habitaciones\n- [1] Añadir habitacion\n" +
              "- [2] Modificar datos de habitacion existente\n- [3] Consultar habitacion mediante identificador\n" +
              "- [4] Consultar habitaciones des/ocupadas\n- [5] Eliminar habitacion del sistema\n" +
              "- [10] Salir de la aplicacion")
        try:
            selector = int(input())

        except ValueError:
            print("Error al introducir el selector")
            break

        if selector == 0:
            print("Mostrando informacion de habitaciones:")
            ListRooms()
        elif selector == 1:
            AddRoomMenu()
        elif selector == 2:
            ModifyRoomMenu()
        elif selector == 3:
            print("Introduce el identificador de la habitación a consultar:")
            idd = int(input())
            ListRoomIdd(idd)
        elif selector == 4:
            print("Deseas mostrar las habitaciones ocupadas o desocupadas? (1=ocupadas, 0=desocupadas)")
            ocup = int(input())
            if ocup == 1:
                print("Mostrando las habitaciones ocupadas")
            else:
                print("Mostrando las habitaciones desocupadas")
            ListRoomsOcupancy(ocup)
        elif selector == 10:
            break

        else:
            print("Selector no valido. Elije una opcion entre las existentes.")

    print("Saliendo de la aplicacion.")

"""
#PRUEBA POST
url2 = 'http://localhost:8080/pruebapost'

data2 = {'name': 'Pablo'}
headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r2 = requests.post(url2, data=json.dumps(data2), headers=headers2)
#data = '"name:":"Pablo"'
#response=requests.post(url2,data=data)
d2=r2.json()
print(d2["data"])

#PRUEBA PUT

url3 = 'http://localhost:8080/pruebaput'

data3 = {'name': 'Pablo'}
headers3 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r3 = requests.put(url3, data=json.dumps(data3), headers=headers3)
d3=r3.json()
print(d3["data"])
"""
