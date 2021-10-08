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
    indexKiller = random.randint(0, 1)
    killer = match.pop(indexKiller)
    killed = match.pop()

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
    matches = []
    leftouts = []

    for city in cities:
        matched, leftout = managePlayers(cities[city]["players"])

        matches.extend(matched)

        if leftout != None:
            leftouts.append(leftout)

    matches.extend(matchLeftouts(cities, leftouts))

    for match in matches:
        killer, _ = fight(match, output)
        cities[killer.city]["players"].append(killer)


def managePlayers(players: List[Player]):
    if len(players) % 2 == 0:
        return makeMatches(players), None
    leftout = players.pop()
    return makeMatches(players), leftout


def makeMatches(players: List[Player]):
    matches = []
    for _ in range(0, int(len(players) / 2)):
        index1 = random.randint(0, (len(players) - 1))
        player1 = players.pop(index1)

        index2 = random.randint(0, (len(players) - 1))
        player2 = players.pop(index2)

        matches.append([player1, player2])
    return matches


def findPlayerByCity(players: List[Player], city: str):
    for player in players:
        if player.city == city:
            return player


def matchLeftouts(cities, leftouts: List[Player]):
    matches = []
    matched = []
    for player in leftouts:
        cityNames = list(map(lambda leftout: leftout.city, leftouts))
        if not(player in matched):
            for neighbor, _ in cities[player.city]["neighbor"]:
                if neighbor in cityNames:
                    player2 = findPlayerByCity(leftouts, neighbor)

                    matched.append(player)
                    matched.append(player2)

                    match = [player, player2]
                    matches.append(match)
                    break

        if not player in matched or (cities[player.city]["neighbor"]) == 0:
            cities[player.city]["players"].append(player)

    return matches
