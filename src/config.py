import networkx as nx

from player import Player
from city import City


JUGADORES = "../data/jugadores.txt"
DISTANCIAS = "../data/distancias.txt"


class Config:
    def __init__(self):
        self.cities = dict()
        self.players = list()
        self.Graph = nx.Graph()

    def load(self):
        with open(JUGADORES, 'r') as jugadores:
            for person in jugadores.readlines():
                personArray = person.strip('\n').split(",")
                name = personArray[0]
                age = personArray[1]
                cityName = personArray[2]

                player = Player(name, cityName, age)

                self.players.append(player)

                if self.cities.get(cityName):
                    self.cities[cityName].add_player(player)
                else:
                    self.cities[cityName] = City(cityName, [player])

                self.Graph.add_node(self.cities[cityName])

        with open(DISTANCIAS, 'r') as distancias:
            for distancia in distancias.readlines():
                distanciaArray = distancia.strip('\n').split(", ")
                self.Graph.add_edge(
                    self.cities[distanciaArray[0]], self.cities[distanciaArray[1]], distance=float(distanciaArray[2]))
