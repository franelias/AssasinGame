import random
from typing import List
from assasin_game import AssasinGame
from config import Config
from graph_process import GraphProcess
from player import Player


def fight(player1: Player, player2: Player):
    return random.choice([player1, player2])


def printKill(killer: Player, victim: Player):
    print(f'{killer.name} eliminó a {victim.name}')


def printWinner(winner: Player):
    print(f'{winner.name} ganó the game')


def killRound(players: List[Player]):
    contrincants = random.sample(players, k=2)

    victim = fight(contrincants[0], contrincants[1])

    players.remove(victim)

    return players


def main():
    config = Config()
    config.load()

    process = GraphProcess(config.Graph, 100)
    process.adjustGraph()

    game = AssasinGame(config)

    game.start()

    # round(cities[2], cities[1])


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
