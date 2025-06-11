from vehiculo import Vehiculo
from basedatos import BaseDatos




elif opcion == "3":
     id_v = int(input("ID VEHICULO: "))
     v = bd.buscar_vehiculo(id_v)
    if v:
     print(f"ID: VEHICULO")