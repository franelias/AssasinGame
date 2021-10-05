import random
from typing import List

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


def readFile():
    cities = {}
    players = []

    with open(JUGADORES, 'r') as jugadores, open(DISTANCIAS, 'r') as distancias:
        for person in jugadores.readlines():
            personArray = person.split(",")
            name = personArray[0]
            age = personArray[1]
            cityName = personArray[2]

            player = Player(name, cityName, age)

            players.append(player)

            if cities.get(cityName):
                cities[cityName].add_player(player)
            else:
                cities[cityName] = City(cityName, [player])

    return cities, players


def fight(player1: Player, player2: Player):
    return random.choice([player1, player2])


def printKill(killer: Player, victim: Player):
    print(f'{killer.name} eliminó a {victim.name}')


def printWinner(winner: Player):
    print(f'{winner.name} ganó the game')


def lastStandInCity(city: City):
    count = 1
    while (len(city.players) > 1):
        killer = random.choice(city.players)

        city.players.remove(killer)

        victim = random.choice(city.players)

        city.players.remove(victim)
        city.players.append(killer)

        count += 1

        printKill(killer, victim)

    return city


def main():
    cities = readFile()
    for key in cities[0]:
        cities[0][key] = lastStandInCity(cities[0][key])


if __name__ == "__main__":
    main()
