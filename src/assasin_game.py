from typing import List
from config import Config

import random

from player import Player


class AssasinGame:
    def __init__(self, config: Config):
        self.players = config.players
        self.cities = config.cities
        self.graph = config.Graph
        self.round = 0

    def start(self):
        while len(self.choosePlayers()[0]) != 0:
            self.playRound()

    def printKill(self, killer: Player, victim: Player):
        print(f'{killer.name} eliminó a {victim.name}')

    def printWinner(self, winner: Player):
        print(f'{winner.name} ganó the game')

    def fight(self, match: List[Player]):
        killed = random.choice(match)
        match.remove(killed)
        self.cities[killed.city].players.remove(killed)

        # self.printKill(match[0], killed)

        return match[0]

    def playRound(self):
        winners = []
        matches = self.choosePlayers()
        for match in matches[0]:
            winner = self.fight(match)
            winners.append(winner)
        for player in matches[1]:
            self.printWinner(player)
        self.players = winners
        self.round += 1
        print(f'ronda {self.round}',
              f'{len(self.players)} personas restantes')

    def choosePlayers(self):
        matches = []
        leftouts = []
        for node in self.graph:
            result = self.get_matches(node.players)
            matches.extend(result[0])
            if result[1] != None:
                leftouts.append(result[1])

        matches.extend(self.matchLeftouts(leftouts))

        return matches, leftouts

    def findOtherPlayer(self, letfouts: List[Player], city: str):
        for player in letfouts:
            if player.city == city:
                return player

    def matchLeftouts(self, leftouts: List[Player]):
        matches = []
        for player in leftouts:
            playerCity = self.cities[player.city]
            for node in self.graph[playerCity]:
                if player in leftouts and player.city != node.name and len(node.players) % 2 != 0:
                    player2 = self.findOtherPlayer(leftouts, node.name)
                    if player2:
                        matches.append([player, player2])
                        leftouts.remove(player)
                        leftouts.remove(player2)
        return matches

    def makeMatches(self, players: List[Player]):
        cityMatches = []
        for _ in range(0, int(len(players) / 2)):
            match = random.sample(players, k=2)
            cityMatches.append(match)
            players.remove(match[0])
            players.remove(match[1])
        return cityMatches

    def get_matches(self, players: List[Player]):
        dummyPlayerList = players.copy()
        if len(players) % 2 == 0:
            return self.makeMatches(dummyPlayerList), None
        p = dummyPlayerList.pop()
        return (self.makeMatches(dummyPlayerList), p)
