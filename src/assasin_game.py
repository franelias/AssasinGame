from typing import Dict, List, Tuple
from config import Config
from city import City

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

    def fight(self, match: List[Player]):
        killed = random.choice(match)
        match.remove(killed)
        self.cities[killed.city].players.remove(killed)

        return match[0]

    def playRound(self):
        winners = []
        matches = self.choosePlayers()
        for match in matches:
            winner = self.fight(match)
            winners.append(winner)
        self.players = winners
        self.round += 1
        print(f'ronda {self.round}',
              f'{len(self.players)} personas restantes')

    def matchLeftouts(self, leftouts: dict):
        matches = []
        # for player in leftouts.values():
        # values = list(self.graph[self.cities[player.city]].values())
        # valuesList = sorted(list(
        #     map(lambda value: value["distance"], values)))
        # for distance in self.graph[self.cities[player.city]]:
        #     print(distance)
        # print(self.graph.__getitem__(self.cities[player.city]))

        # if city.players % 2 != 0:
        #     matches.append([player, ])

        return matches

    def choosePlayers(self):
        matches = []
        leftouts = {}
        for node in self.graph:
            result = self.get_matches(node.players)
            matches.extend(result[0])
            if result[1] != None:
                leftouts[node] = result[1]

        matches.extend(self.matchLeftouts(leftouts))

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
