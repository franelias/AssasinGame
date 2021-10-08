import sys
from player import Player

# Estructura de representación de una ciudad
# {
#     Rosario: {
#         neighbor: [
#             (
#                 Buenos Aires: 21
#             ),
#             (
#                 La Pampa: 420
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
#     }
# }


def inputMaxDistance():
    n = float(input('Ingresa la distancia pa: '))
    return n


def loadPlayersFromFile(cities: dict):
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


def loadCitiesFromFile(cities: dict, n: int):
    distanceFile = sys.argv[-1]
    with open(distanceFile, 'r') as distancias:
        for distancia in distancias.readlines():
            distanciaArray = distancia.strip('\n').split(", ")

            if float(distanciaArray[2]) < n:
                cities[distanciaArray[0]]["neighbor"].append(
                    [distanciaArray[1], distanciaArray[2]])
                cities[distanciaArray[1]]["neighbor"].append(
                    [distanciaArray[0], distanciaArray[2]])
