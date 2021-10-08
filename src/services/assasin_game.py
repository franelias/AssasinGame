from io import TextIOWrapper
import random
from typing import List
from player import Player


def start(cities: dict, output: TextIOWrapper):
    while canPlay(cities):
        playRound(cities, output)

    for city in cities:
        for player in cities[city]["players"]:
            printWinner(player, output)


def printWinner(winner: Player, output: TextIOWrapper):
    output.write(f'{winner.name} ganó the game\n')


def printKill(killer: Player, killed: Player, output: TextIOWrapper):
    output.write(f'{killer.name} mató a {killed.name}\n')


def fight(match: List[Player], output: TextIOWrapper):
    indexKilled = 0
    indexKiller = random.randint(0, 1)

    if indexKiller == 0:
        indexKilled = 1

    killer = match[indexKiller]
    killed = match.pop(indexKilled)

    printKill(killer, killed, output)

    return killer, killed


def canPlay(cities):
    for city in cities:
        if len(cities[city]["players"]) >= 2:
            return True
        if len(cities[city]["players"]) == 1:
            for neighbor, _ in cities[city]["neighbor"]:
                if len(cities[neighbor]["players"]) >= 1:
                    return True
    return False


def playRound(cities, output: TextIOWrapper):
    leftouts = []

    for city in cities:
        leftout = managePlayers(cities[city]["players"], output)

        if leftout != None:
            leftouts.append(leftout)

    matchLeftouts(cities, leftouts, output)


def managePlayers(players: List[Player], output: TextIOWrapper):
    if len(players) % 2 == 0:
        players.extend(makeFights(players, output))
        return None
    leftout = players.pop()
    players.extend(makeFights(players, output))
    players.append(leftout)
    return leftout


def makeFights(players: List[Player], output: TextIOWrapper):
    matchWinners = []

    for _ in range(0, int(len(players) / 2)):
        index1 = random.randint(0, (len(players) - 1))

        player1 = players[index1]
        players.pop(index1)

        index2 = random.randint(0, (len(players) - 1))
        player2 = players[index2]
        players.pop(index2)

        killer, _ = fight([player1, player2], output)
        matchWinners.append(killer)

    return matchWinners


def findPlayerByCity(players: List[Player], city: str):
    for player in players:
        if player.city == city:
            return player


def matchLeftouts(cities, leftouts: List[Player], output: TextIOWrapper):
    for player in leftouts:
        for neighbor, _ in cities[player.city]["neighbor"]:
            cityNames = map(lambda leftout: leftout.city, leftouts)

            if neighbor in list(cityNames):
                player2 = findPlayerByCity(leftouts, neighbor)
                if player2:
                    leftouts.remove(player)
                    leftouts.remove(player2)

                    match = [player, player2]
                    winner, _ = fight(match, output)

                    cities[winner.city]["players"].remove(winner)
                    break
