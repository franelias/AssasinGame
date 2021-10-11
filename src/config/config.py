import sys
from typing import Dict, List, Tuple
from player import Player

# Estructura de representación de una ciudad, denominada Cities:
# {
#     Rosario: {
#         neighbor: [
#             (
#                 Buenos Aires, 21
#             )
#         ],
#         adultPlayers: [
#             "pepe",
#             "culiana"
#         ],
#         minorPlayers: [
#             "pepe",
#             "culiana"
#         ]
#     },
#     Buenos Aires: {
#         neighbor: [
#             (
#                 Rosario, 21
#             )
#         ],
#         adultPlayers: [
#             "juan",
#         ],
#         minorPlayers: [
#             "carlos",
#         ]
#     }
# }

# Declaración de la estructura de datos.
City = Dict[str, List]
Cities = Dict[str, City]

# Función que imprime un mensaje en pantalla y espera un número que representará la distancia máxima
# posible entre ciudades, luego lo retorna.
# main: None -> float


def inputMaxDistance():
    n = float(input('Ingrese la distancia máxima entre ciudades: '))
    return n

# Función que toma una estructura de tipo Cities y lo llena con datos del archivos de jugadores
# loadPlayersFromFile: Cities -> None


def loadPlayersFromFile(cities: Cities):
    playerFile = sys.argv[-2]

    with open(playerFile, 'r') as jugadores:
        for person in jugadores.readlines():
            personArray = person.strip('\n').split(",")
            name = personArray[0]
            age = personArray[1]
            cityName = personArray[2]

            player = Player(name, cityName, age)

            if int(player.age) > 18:
                cities.setdefault(
                    cityName, {"neighbor": [], "adultPlayers": [player], "minorPlayers": []})["adultPlayers"].append(player)
            else:
                cities.setdefault(
                    cityName, {"neighbor": [], "adultPlayers": [], "minorPlayers": [player]})["minorPlayers"].append(player)

# Función que toma una estructura de tipo Cities y un número y llena la misma con datos del archivos de distancias ingresado
# por argumento al correr el programa.
# loadCitiesFromFile: Cities float -> None


def loadCitiesFromFile(cities: Cities, n: float):
    distanceFile = sys.argv[-1]
    with open(distanceFile, 'r') as distancias:
        for distancia in distancias.readlines():
            distanciaArray = distancia.strip('\n').split(", ")

            if float(distanciaArray[2]) < n:
                cities[distanciaArray[0]]["neighbor"].append(
                    [distanciaArray[1], distanciaArray[2]])
                cities[distanciaArray[1]]["neighbor"].append(
                    [distanciaArray[0], distanciaArray[2]])
