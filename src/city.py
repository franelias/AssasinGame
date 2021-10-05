from typing import List

from player import Player


class City:
    def __init__(self, name: str, players: List[Player]):
        self.name = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)
