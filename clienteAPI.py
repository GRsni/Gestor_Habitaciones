import requests, json

urlBase = 'http://localhost:8080'

urlAdd = '/AddRoom'
urlListAll = '/ListRooms'


def AddRoom(plazas, precio):
    # INSERTA 1 HABITACIÓN
    data2 = {'plazas': plazas, 'precio': precio}
    headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r2 = requests.post(str(urlBase + urlAdd), data=json.dumps(data2), headers=headers2)
    d2 = r2.json()
    print("Id de habitacion insertada: " + str(d2['idd']))


def ListarHabitaciones():
    # LISTA LAS HABITACIONES
    response = requests.get(str(urlBase + urlListAll))
    d = response.json()
    for r in d:
        print('idd: ' + str(r['idd']) + ' plazas: ' + str(r['plazas']) + ' precio: ' +
              str(r['precio']) + ' €\nOcupada: ' + str(r['ocupada']) + "\n")


def ParseEquipment(array):
    material = ("Armario grande", "Aire acondicionado", "Caja fuerte", "Escritorio", "WiFi")
    output = ""
    for i in array:
        if i == 1:
            output += material[i] + ", "

    return output


if __name__ == "__main__":
    while True:
        print("\nElije la operación a realizar:\n- [0] Listar todas las habitaciones:0\n- [1] Añadir habitacion:1\n" +
              "- [2] Modificar datos de habitacion existente\n- [3] Consultar habitacion mediante identificador:")
        selector = int(input())

        if selector == 0:
            ListarHabitaciones()
        elif selector == 1:
            print("Introduce las plazas de la habitacion:")
            plazas = int(input())
            print("Introduce el precio por noche:")
            precio = int(input())
            AddRoom(plazas, precio)
        elif selector == 2:
            print("Introduce el identificador de la habitacion a modificar:")
        elif selector == 3:
            print("Introduce el identificador de la habitación a consultar:")
            


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
