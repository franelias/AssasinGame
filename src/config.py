from player import Player

JUGADORES = "./data/jugadores.txt"
DISTANCIAS = "./data/distancias.txt"

# Estructura del grafo
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


class Config:
    def __init__(self, players: str, distances: str):
        self.graph = dict()
        self.players = players
        self.distances = distances

    def loadPlayers(self):
        with open(self.players, 'r') as jugadores:
            for person in jugadores.readlines():
                personArray = person.strip('\n').split(",")
                name = personArray[0]
                age = personArray[1]
                cityName = personArray[2]

                player = Player(name, cityName, age)

                if int(player.age) > 18:
                    self.graph.setdefault(
                        cityName, {"neighbor": [], "adultPlayers": [player], "minorPlayers": []})["adultPlayers"].append(player)
                else:
                    self.graph.setdefault(
                        cityName, {"neighbor": [], "adultPlayers": [], "minorPlayers": [player]})["minorPlayers"].append(player)

    def loadGraph(self, n: int):
        with open(self.distances, 'r') as distancias:
            for distancia in distancias.readlines():
                distanciaArray = distancia.strip('\n').split(", ")

                if float(distanciaArray[2]) < n:
                    self.graph[distanciaArray[0]]["neighbor"].append(
                        [distanciaArray[1], distanciaArray[2]])
                    self.graph[distanciaArray[1]]["neighbor"].append(
                        [distanciaArray[0], distanciaArray[2]])
