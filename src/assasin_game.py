import random
from typing import List
from config import Config
from player import Player


class AssasinGame:
    def __init__(self, config: Config):
        self.graph = config.graph

    def start(self):
        while self.canPlay():
            self.playRound()

    def printWinner(self, winner: Player):
        print(f'{winner.name} ganó the game')

    def fight(self, match: List[Player]):
        killed = random.choice(match)
        match.remove(killed)

        # self.printKill(match[0], killed)

        return match[0], killed

    def canPlay(self):
        for city in self.graph:
            if len(self.graph[city]["players"]) >= 2:
                return True
            if len(self.graph[city]["players"]) == 1:
                for neighbor in self.graph[city]["neighbor"]:
                    # neighborName = (list(neighbor.keys()))[0]

                    if len(self.graph[neighbor[0]]["players"]) >= 1:
                        return True
        return False

    def playRound(self):
        leftouts = []

        for city in self.graph:
            leftout = self.managePlayers(self.graph[city]["players"])

            if leftout != None:
                leftouts.append(leftout)

        self.matchLeftouts(leftouts)

    def managePlayers(self, players: List[Player]):
        if len(players) % 2 == 0:
            players.extend(self.makeFights(players))
            return None
        leftout = players.pop()
        players.extend(self.makeFights(players))
        players.append(leftout)
        return leftout

    def makeFights(self, players: List[Player]):
        matchWinners = []
        matches = []
        # start_time = time.time()

        for _ in range(0, int(len(players) / 2)):
            index1 = random.randint(0, (len(players) - 1))

            player1 = players[index1]
            players.pop(index1)

            index2 = random.randint(0, (len(players) - 1))
            player2 = players[index2]
            players.pop(index2)

            matches.append([player1, player2])

        for match in matches:
            winner = self.fight(match)
            matchWinners.append(winner[0])

        return matchWinners

    def findOtherPlayer(self, leftouts: List[Player], city: str):
        for player in leftouts:
            if player.city == city:
                return player

    def matchLeftouts(self, leftouts: List[Player]):
        for player in leftouts:
            for neighbor in self.graph[player.city]["neighbor"]:
                cityNames = map(lambda leftout: leftout.city, leftouts)

                if neighbor[0] in list(cityNames):
                    # print("MATCH", player.city, neighbor[0])
                    player2 = self.findOtherPlayer(leftouts, neighbor[0])
                    if player2:
                        leftouts.remove(player)
                        leftouts.remove(player2)

                        match = [player, player2]
                        winner = self.fight(match)

                        self.graph[winner[1].city]["players"].remove(winner[1])
                        break
