from typing import List, Tuple
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
        while self.choosePlayers() != None:
            self.playRound()

    def playRound(self):
        matches = self.choosePlayers()
        winners = []
        for match in matches:
            winner = self.figth(match)
            winners.append(winner)
        self.players = winners
        self.round += 1
        # print(f'ronda {ronda}', f'{len(self.players)} personas restantes')

    def choosePlayers(self) -> List[Tuple[Player]]:
        result = []
        for node in self.graph:
            get_matches(node.players)
            couples = random.sample(node.players, k=2)
            result.append(couples)

        # for node in self.graph:
        #     if len(node.self.players) > 1:
        #         self.choosePlayers(node, self.players)
        #     else:
        #         print(f'mmm llegue a 1 mamá {node.name}')
        #         sorted_neightbors = list(filter(lambda element: isinstance(element, City), sorted(
        #             self.graph[node].items(), key=lambda item: item[1]["distance"])))

        #         sorted_neightbors2 = sorted(
        #             self.graph[node].items(), key=lambda item: item[1]["distance"])

        #         print(sorted_neightbors)
        #         print(sorted_neightbors2)
        #         print(isinstance(sorted_neightbors2[0], City))

        #         players_pool = node.players + \
        #             sorted_neightbors[0].players

        #         player1 = random.choice(players_pool)
        #         players_pool.remove(player1)

        #         player2 = random.choice(players_pool)

        #         result = self.fight(player1, player2)

        #         self.players.remove(player2)

        #         if player2 != node.self.players[0]:
        #             sorted_neightbors[0].self.players.remove(player2)
        #         else:
        #             node.self.players.remove(player2)

    def fight(self):
        pass

    def get_matches(list):
        if len(list) % 2 == 0:
            return (random.sample(list, k=2), None)
        p = list.removeFirst()
        return (random.sample(list, k=2, p)
