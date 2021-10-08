import random
from assasin_game import AssasinGame
from config import Config
# from graph_process import GraphProcess
import time
import sys


def main():
    start_time = time.time()
    # -2 players -1 distancias
    config = Config(sys.argv[-2], sys.argv[-1])
    config.loadPlayers()
    config.loadGraph(100)

    # print(config.graph)

    # process = GraphProcess(config.Graph, 100)
    # process.adjustGraph()

    # new_key = "A"
    # old_key = "a"
    # adultPlayers = config.graph["adultPlayers"]
    # minorPlayers = config.graph["minorPlayers"]

    for city in config.graph:
        config.graph[city]["players"] = config.graph[city].pop("adultPlayers")

    adultGame = AssasinGame(config)
    adultGame.start()

    print("aca van lo pibe")

    for city in config.graph:
        config.graph[city]["players"] = config.graph[city].pop("minorPlayers")

        # print(len(config.graph[city]["players"]))

    minorGame = AssasinGame(config)
    minorGame.start()

    # print("end game --- %s seconds ---" % (time.time() - start_time))

    # round(cities[2], cities[1])
    print("--- %s seconds ---" % (time.time() - start_time))


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
