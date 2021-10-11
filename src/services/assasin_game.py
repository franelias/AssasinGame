import random
from io import TextIOWrapper
from typing import List
from player import Player
from config.config import Cities

# Función que administra el sistema de rondas del juego, cuando no
# haya mas parejas para poder seguir jugando, imprime a los ganadores.
# start: Cities TextIOWrapper -> None


def start(cities: Cities, output: TextIOWrapper):
    while canPlay(cities):
        playRound(cities, output)

    printWinners(cities, output)

    return cities


# printWinners: Player TextIOWrapper -> None
# Función que escribe en un archivo los ganadores.
def printWinners(cities: Player, output: TextIOWrapper):
    for city in cities:
        for winner in cities[city]["players"]:
            output.write(f'{winner.name} ganó the game\n')

# Función que escribe en un archivo, el registro de una muerte entre un asesino y un muerto.
# printKill: Player Player TextIOWrapper -> None


def printKill(killer: Player, killed: Player, output: TextIOWrapper):
    output.write(f'{killer.name} mató a {killed.name}\n')


# Función que escoje de una lista de dos jugadores quien sobrevive y quien muere, luego
# lo escribe en un archivo.
# fight: List[Player] TextIOWrapper -> Tuple[Player, Player]
def fight(match: List[Player], output: TextIOWrapper):
    random.shuffle(match)
    killer = match.pop()
    killed = match.pop()
    printKill(killer, killed, output)

    return killer, killed

# Función que devuelve True si se pueden formar parejas con el estado actual de
# las ciudades y sus jugadores, False en caso contrario.
# canPlay: Cities -> bool


def canPlay(cities: Cities):
    for city in cities:
        if len(cities[city]["players"]) >= 2:
            return True
        if len(cities[city]["players"]) == 1:
            for neighbor, _ in cities[city]["neighbor"]:
                if len(cities[neighbor]["players"]) >= 1:
                    return True
    return False

# Función que juega una ronda con el estado actual de las ciudades y sus jugadores.
# playRound: Cities TextIOWrapper -> None


def playRound(cities: Cities, output: TextIOWrapper):
    leftouts = []

    for city in cities:
        leftout = managePlayers(cities[city]["players"], output)

        if leftout != None:
            leftouts.append(leftout)

    matchLeftouts(cities, leftouts, output)

# Función que evalua si la ciudad en cuestión va a tener un Jugador sin pareja
# Caso afirmativo, la remueve de la lista y hace pelear al resto de jugadores entre si, luego lo retorna.
# Caso negativo, hace pelear a los jugadores que estén entre si.
# En cualquiera de los dos casos, la lista original de jugadores por ciudad se sobrescribe con
# la lista de solamente los ganadores de cada enfrentamiento.
# managePlayers: List[Player] TextIOWrapper -> Player | None


def managePlayers(players: List[Player], output: TextIOWrapper):
    if len(players) % 2 == 0:
        players.extend(makeFights(players, output))
        return None
    leftout = players.pop()
    players.extend(makeFights(players, output))
    return leftout

# Función que va formando parejas de a dos de forma aleatoria con los elementos de una lista de jugadores
# y los hace pelear entre si. Retorna una lista con los jugadores
# que ganaron sus respectivos enfrentamientos.
# managePlayers: List[Player] TextIOWrapper -> List[Players]


def makeFights(players: List[Player], output: TextIOWrapper):
    matchWinners = []
    random.shuffle(players)

    for _ in range(0, int(len(players) / 2)):
        player1 = players.pop()
        player2 = players.pop()

        killer, _ = fight([player1, player2], output)
        matchWinners.append(killer)

    return matchWinners

# Función auxiliar que toma una lista de jugadores y el nombre de una ciudad.
# Retorna si existe el jugador de la lista que vive en la ciudad dicha,
# None si no se encuentra en la misma.
# findPlayerByCity: List[Player] str -> Player | None


def findPlayerByCity(players: List[Player], cityName: str):
    for player in players:
        if player.city == cityName:
            return player

# Función que recibe una estructura de tipo Cities, una lista de jugadores sin pareja y una variable de archivo.
# Intenta formar parejas con los jugadores con el siguiente criterio:
    # Si la ciudad del jugador tiene vecinos, busca el más cercano. Si el mismo tiene al menos un jugador, forma una pareja con los dos.
    # Caso contrario, sigue con los restantes.

    # Si se encuentra una pareja, se los hace pelear. Al ganador se los reintegra a la lista de jugadores original, para matchear con
    # otra persona en la siguiente ronda.

    # En el caso de que no encuentre una pareja acorde, o la ciudad del jugador no posea vecinos,
    # reintegra al jugador a la lista de jugadores original.
# matchLeftouts: Cities List[Player] TextIOWrapper -> None


def matchLeftouts(cities: Cities, leftouts: List[Player], output: TextIOWrapper):
    while leftouts:
        match = []

        cityNames = list(map(lambda leftout: leftout.city, leftouts))
        player1 = leftouts.pop()

        for neighbor, _ in cities[player1.city]["neighbor"]:
            if neighbor in cityNames:
                player2 = findPlayerByCity(leftouts, neighbor)
                leftouts.remove(player2)

                match = [player1, player2]
                break

        if match:
            killer, _ = fight(match, output)
            cities[killer.city]["players"].append(killer)
        else:
            cities[player1.city]["players"].append(player1)
