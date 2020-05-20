import requests, json

urlBase = 'http://localhost:8080'

urlAdd = '/AddRoom'
urlListAll = '/ListRooms'
urlModify = '/ModifyRoom'
urlListIdd = '/ListRoomIdd'


def add_room_menu():
    print("Introduce las plazas de la habitacion:")
    plazas = int(input())
    print("Introduce el precio por noche:")
    precio = int(input())
    print("¿Tiene armario? (1=SI / Otro caso=NO)")
    arm = bool(input() == '1')
    print("¿Tiene aire acondicionado? (1=SI / Otro caso=NO)")
    ac = bool(input() == '1')
    print("¿Tiene caja fuerte? (1=SI / Otro caso=NO)")
    cf = bool(input() == '1')
    print("¿Tiene escritorio? (1=SI / Otro caso=NO)")
    esc = bool(input() == '1')
    print("¿Tiene wifi? (1=SI / Otro caso=NO)")
    wifi = bool(input() == '1')
    add_room(plazas, precio, arm, ac, cf, esc, wifi)


def add_room(plazas, precio, armario, ac, cajafuerte, escritorio, wifi):
    # INSERTA 1 HABITACIÓN
    data2 = {'plazas': plazas, 'precio': precio, 'armario': armario, 'ac': ac, 'cajafuerte': cajafuerte,
             'escritorio': escritorio, 'wifi': wifi}
    headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r2 = requests.post(str(urlBase + urlAdd), data=json.dumps(data2), headers=headers2)
    d2 = r2.json()
    print("Id de habitacion insertada: " + str(d2['idd']))


def get_room_string_from_json(data):
    out = 'idd: ' + str(data['idd']) + ' plazas: ' + str(data['plazas']) + ' precio: ' + \
          str(data['precio']) + ' € Ocupada: '
    out += str(data['ocupada'])
    out += '\n EQUIPAMIENTO: \n'
    if data['armario']:
        out += '\t- armario \n'
    if data['ac']:
        out += '\t- aire acondicionado \n'
    if data['cajafuerte']:
        out += '\t- caja fuerte \n'
    if data['escritorio']:
        out += '\t- escritorio \n'
    if data['wifi']:
        out += '\t- wifi \n'
    return out


def list_rooms():
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListAll))
    d = response.json()

    for r in d:
        print(get_room_string_from_json(r))


def list_room_by_id(idd):
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListIdd + '/' + str(idd)))
    r = response.json()
    print(get_room_string_from_json(r))


def list_rooms_by_occupancy(ocup):
    response = requests.get(str(urlBase) + str(urlListAll))
    rooms = response.json()
    for r in rooms:
        if r['ocupada'] == ocup:
            print(get_room_string_from_json(r))


def modify_room_menu():
    arm = ac = cf = esc = wifi = 0
    print("Introduce el identificador de la habitacion a modificar:")
    idd = int(input())
    print("Introduzca nuevo nº de plazas (0 si no desea modificar)")
    plazas = int(input())
    print("Introduce nuevo precio por noche (0 si no desea modificar)")
    precio = int(input())
    print("¿Se encuentra ocupada actualmente? (1=SI / Otro caso=NO)")
    ocupada = bool(input() == '1')
    print("¿Desea cambiar el equipamiento? (1=SI / Otro caso=NO)")
    op = int(input())
    if op == 1:
        print("¿Tiene armario? (1=SI / Otro caso=NO)")
        arm = bool(input() == '1')
        print("¿Tiene aire acondicionado? (1=SI / Otro caso=NO)")
        ac = bool(input() == '1')
        print("¿Tiene caja fuerte? (1=SI / Otro caso=NO)")
        cf = bool(input() == '1')
        print("¿Tiene escritorio? (1=SI / Otro caso=NO)")
        esc = bool(input() == '1')
        print("¿Tiene wifi? (1=SI / Otro caso=NO)")
        wifi = bool(input() == '1')
    modify_room(idd, plazas, precio, ocupada, op, arm, ac, cf, esc, wifi)


def modify_room(idd, plazas, precio, ocupada, op, arm, ac, cf, esc, wifi):
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
            continue

        if selector == 0:
            print("Mostrando informacion de habitaciones:")
            list_rooms()
        elif selector == 1:
            add_room_menu()
        elif selector == 2:
            modify_room_menu()
        elif selector == 3:
            print("Introduce el identificador de la habitación a consultar:")
            idd = int(input())
            list_room_by_id(idd)
        elif selector == 4:
            print("Deseas mostrar las habitaciones ocupadas o desocupadas? (1=ocupadas, 0=desocupadas)")
            ocup = bool(input() == '1')
            if ocup == 1:
                print("Mostrando las habitaciones ocupadas")
            else:
                print("Mostrando las habitaciones desocupadas")
            list_rooms_by_occupancy(ocup)
        elif selector == 10:
            break

        else:
            print("Selector no valido. Elije una opcion entre las existentes.")

    print("Saliendo de la aplicacion.")

