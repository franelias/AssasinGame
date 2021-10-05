import random
from typing import List
import networkx as nx
from networkx.classes import graph
from collections import OrderedDict

JUGADORES = ".\jugadores.txt"
DISTANCIAS = ".\distancias.txt"


class Player:
    def __init__(self, name: str,  city: str, age: int):
        self.name = name
        self.city = city
        self.age = age


class City:
    def __init__(self, name: str, players: List[Player]):
        self.name = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)


def readFile(maxDistance: int):
    cities = OrderedDict()
    players = []
    G = nx.Graph()
    with open(JUGADORES, 'r') as jugadores:
        for person in jugadores.readlines():
            personArray = person.strip('\n').split(",")
            name = personArray[0]
            age = personArray[1]
            cityName = personArray[2]

            player = Player(name, cityName, age)

            players.append(player)

            if cities.get(cityName):
                cities[cityName].add_player(player)
            else:
                cities[cityName] = City(cityName, [player])

            G.add_node(cities[cityName])

    with open(DISTANCIAS, 'r') as distancias:
        for distancia in distancias.readlines():
            distanciaArray = distancia.strip('\n').split(", ")
            if float(distanciaArray[2]) < maxDistance:
                G.add_edge(
                    cities[distanciaArray[0]], cities[distanciaArray[1]], distance=float(distanciaArray[2]))

    return cities, players, G


def fight(player1: Player, player2: Player):
    return random.choice([player1, player2])


def printKill(killer: Player, victim: Player):
    print(f'{killer.name} eliminó a {victim.name}')


def printWinner(winner: Player):
    print(f'{winner.name} ganó the game')


def choosePlayers(city: City, players: list):
    killer = random.choice(city.players)

    city.players.remove(killer)

    victim = random.choice(city.players)

    city.players.remove(victim)
    city.players.append(killer)

    players.remove(victim)

    # printKill(killer, victim)


def round(G: graph, players: list):
    ronda = 0
    for _ in range(len(players)):
        for node in G:
            if len(node.players) > 1:
                choosePlayers(node, players)
            else:
                print(f'mmm llegue a 1 mamá {node.name}')
                sorted_neightbors = list(filter(lambda element: isinstance(element, City), sorted(
                    G[node].items(), key=lambda item: item[1]["distance"])))

                sorted_neightbors2 = sorted(
                    G[node].items(), key=lambda item: item[1]["distance"])

                print(sorted_neightbors)
                print(sorted_neightbors2)
                print(isinstance(sorted_neightbors2[0], City))

                players_pool = node.players + sorted_neightbors[0].players

                player1 = random.choice(players_pool)
                players_pool.remove(player1)

                player2 = random.choice(players_pool)

                result = fight(player1, player2)

                players.remove(player2)

                if player2 != node.players[0]:
                    sorted_neightbors[0].players.remove(player2)
                else:
                    node.players.remove(player2)
        ronda += 1
        print(f'ronda {ronda}', f'{len(players)} personas restantes')


def main():
    cities = readFile(100)

    for node in cities[2]:
        print(dict(sorted(cities[2][node].items(),
                          key=lambda item: item[1]["distance"])))

        break

    round(cities[2], cities[1])


if __name__ == "__main__":
    main()


# def game(cities, players, max):
#     while(cond):
#         player1 = random.choice(players)
#         playerCity = cities[player1.city]
#         if cities[player1.city].players > 1:
#             player2 = random.choice(cities[player1.city].players)
#             result = fight(player1, player2)
#             if not result: #aka perdio
#               players.remove(player1)
#               playerCity.players.remove(player1)
#             else:
#               players.remove(player2)
#               playerCity.players.remove(player2)
#         elif tiene vecino?(player1.city):
#             neightbour = random.choice(vecinos(player1.city))
#             player2 = random.choice(neightbour.players)
#         elif player2?:
#             result = fight(player1, player2)
#             if not result: #aka perdio
#               players.remove(player1)
#               playerCity.players.remove(player1)
#             else:
#               players.remove(player2)
#               playerCity.players.remove(player2)
