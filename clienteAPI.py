import requests, json


url2 = 'http://localhost:8080/PedirHabitacion'

#INSERTA 1 HABITACIÓN

data2 = {'plazas' : '2','precio' : '80'}
headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r2 = requests.post(url2, data=json.dumps(data2), headers=headers2)
d2=r2.json()
print(d2['idd'])

#INSERTA OTRA HABITACIÓN
data2 = {'plazas' : '5','precio' : '30'}
headers2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r2 = requests.post(url2, data=json.dumps(data2), headers=headers2)
d2=r2.json()
print(d2['idd'])



#LISTA LAS HABITACIONES

url = 'http://localhost:8080/ListRooms'

response = requests.get(url)
d=response.json()
for r in d:
    print('idd: '+str(r['idd'])+' value: '+str(r['plazas'])+' precio: '+str(r['precio'])+' \n')


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
