import requests, json

urlBase = 'http://localhost:8080'

urlAdd = '/AddRoom'
urlListAll = '/ListRooms'
urlModify='/ModifyRoom'
urlListIdd='/ListRoomIdd'


def AddRoom(plazas, precio, armario, ac, cajafuerte, escritorio, wifi):
    # INSERTA 1 HABITACIÓN
    data2 = {'plazas': plazas, 'precio': precio, 'armario': armario, 'ac': ac, 'cajafuerte': cajafuerte,
             'escritorio': escritorio, 'wifi': wifi}
    headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r2 = requests.post(str(urlBase + urlAdd), data=json.dumps(data2), headers=headers2)
    d2 = r2.json()
    print("Id de habitacion insertada: " + str(d2['idd']))


def ListarHabitaciones():
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListAll))
    d = response.json()
    for r in d:
        out = 'idd: ' + str(r['idd']) + ' plazas: ' + str(r['plazas']) + ' precio: ' + str(
            r['precio']) + ' € Ocupada: '
        if r['ocupada']==1:
            out+=' si '
        else:
            out+=' no'
        out+= '\n EQUIPAMIENTO: \n'
        if r['armario'] == 1:
            out += '\t- armario \n'
        if r['ac'] == 1:
            out += '\t- aire acondicionado \n'
        if r['cajafuerte'] == 1:
            out += '\t- caja fuerte \n'
        if r['escritorio'] == 1:
            out += '\t- escritorio \n'
        if r['wifi'] == 1:
            out += '\t- wifi \n'
        print(out)


def ListRoomIdd(idd):
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListIdd+'/'+str(idd)))
    r = response.json()
    out = 'idd: ' + str(r['idd']) + ' plazas: ' + str(r['plazas']) + ' precio: ' + str(
        r['precio']) + ' € Ocupada: '
    if r['ocupada'] == 1:
        out += ' si '
    else:
        out += ' no'
    out += '\n EQUIPAMIENTO: \n'
    if r['armario'] == 1:
        out += '\t- armario \n'
    if r['ac'] == 1:
        out += '\t- aire acondicionado \n'
    if r['cajafuerte'] == 1:
        out += '\t- caja fuerte \n'
    if r['escritorio'] == 1:
        out += '\t- escritorio \n'
    if r['wifi'] == 1:
        out += '\t- wifi \n'
    print(out)


def ModifyRoom(idd,plazas,precio,ocupada,op,arm,ac,cf,esc,wifi):
    data = {'plazas': plazas, 'precio': precio,'ocupada':ocupada,'op':op, 'armario': arm, 'ac': ac, 'cajafuerte': cf,
             'escritorio': esc, 'wifi': wifi}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.put(str(urlBase + urlModify+'/'+str(idd)), data=json.dumps(data), headers=headers)
    d = r.json()
    print("Id de habitacion modificada: " + str(d['idd']))


if __name__ == "__main__":
    while True:
        print("\nElije la operación a realizar:\n- [0] Listar todas las habitaciones\n- [1] Añadir habitacion\n" +
              "- [2] Modificar datos de habitacion existente\n- [3] Consultar habitacion mediante identificador:")
        selector = int(input())

        if selector == 0:
            ListarHabitaciones()
        elif selector == 1:
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
        elif selector == 2:
            arm=0
            ac=0
            cf=0
            esc=0
            wifi=0
            print("Introduce el identificador de la habitacion a modificar:")
            idd=int(input())
            print("Introduzca nuevo nº de plazas (0 si no desea modificar)")
            plazas=int(input())
            print("Introduce nuevo precio por noche (0 si no desea modificar)")
            precio=int(input())
            print("¿Se encuentra ocupada actualmente? (1=si 0=no)")
            ocupada = int(input())
            print("¿Desea cambiar el equipamiento? (1=si 0=no)")
            op=int(input())
            if op==1:
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
            ModifyRoom(idd,plazas,precio,ocupada,op,arm,ac,cf,esc,wifi)

        elif selector == 3:
            print("Introduce el identificador de la habitación a consultar:")
            idd=int(input())
            ListRoomIdd(idd)

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
