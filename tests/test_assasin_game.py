from src.services.assasin_game import canPlay, printWinners, fight, findPlayerByCity, makeFights, managePlayers, matchLeftouts, playRound, start
from src.player import Player
from typing import List
import sys
sys.path.append("/src")

# Función auxiliar para crear un output file para testing


def create_test_output():
    output = open("../tests/data/output.txt", "w+")

    return output

# Función auxiliar que genera una lista de jugadores para testear


def players_list(city: str):
    players = [
        Player('Juan', city, 20),
        Player('Juana', city, 40),
        Player('Juanita', city, 60)
    ]

    return players


def test_start():

    testDict = {
        'Rosario': {
            'neighbor': [],
            'players': players_list('Rosario'),
        },
    }

    output = create_test_output()

    start(testDict, output)

    assert len(testDict['Rosario']['players']) == 1


def test_printWinenrs():
    playersList = players_list('Rosario')
    testDict = {
        'Rosario': {
            'neighbor': [],
            'players': playersList,
        },
    }

    output = create_test_output()

    printWinners(testDict, output)

    output.seek(0)  # Muevo el puntero al inicio del archivo

    i = 0
    for line in output.readlines():
        assert line == f'{playersList[i].name} ganó\n'
        i += 1

    output.close()


def test_fight():
    # Testeo que fight me devuelva 2 jugadores
    player1 = Player('Juan', 'Rosario', 20)
    player2 = Player('Maria', 'Funes', 69)

    output = create_test_output()

    result = fight([player1, player2], output)

    output.seek(0)  # Muevo el puntero al inicio del archivo

    line = output.readlines()[0]

    assert (line == f'{player1.name} mató a {player2.name}\n' or line ==
            f'{player2.name} mató a {player1.name}\n')
    assert len(result) == 2

    output.close()


def test_canPlay():
    # Testeo que me deje jugar cuando haya jugadores

    # Este puede jugar
    testDict = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                )
            ],
            'players': players_list('Rosario'),
        },

        'CABA': {
            'neighbor': [
                (
                    'Rosario', 400
                )
            ],
            'players': players_list('CABA')
        }
    }

    # Este no puede jugar
    testDict2 = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                )
            ],
            'players': [Player('Juan', 'Rosario', 20)],
        },

        'CABA': {
            'neighbor': [
                (
                    'Rosario', 400
                )
            ],
            'players': []
        }
    }

    testDict3 = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                )
            ],
            'players': [Player('Juan', 'Rosario', 20)],
        },

        'CABA': {
            'neighbor': [
                (
                    'Rosario', 400
                )
            ],
            'players': players_list('CABA')
        }

    }

    bool1 = canPlay(testDict)
    bool2 = canPlay(testDict2)
    bool3 = canPlay(testDict3)

    assert bool1 and (not bool2) and bool3


def test_playRound():
    # Testeo una ronda del juego
    testDict = {
        'Rosario': {
            'neighbor': [],
            'players': players_list('Rosario'),
        }
    }

    output = create_test_output()

    playRound(testDict, output)

    assert len(testDict['Rosario']['players']) == 2


def test_managePlayers():
    # Testeo que la función me devuelva el jugador que queda vivo de la lista

    output = create_test_output()

    playerList = players_list('Rosario')

    result = managePlayers(playerList, output)

    assert type(result) == Player
    assert len(playerList) == 1

    playerList = players_list('Sante Fe')
    playerList.append(Player('Maria', 'Sante Fe', 44))

    result = managePlayers(playerList, output)

    assert len(playerList) == 2
    assert type(result) == type(None)


def test_makeFights():
    # Testeo que me devuelva una lista de jugadores
    output = create_test_output()

    result = makeFights(players_list('Rosario'), output)
    assert type(result) == list

    for element in result:
        assert type(element) == Player


def test_findPlayerByCity():
    players = [Player('Juan', 'Rosario', 20), Player(
        'Maria', 'Funes', 69), Player('Maria', 'Sante Fe', 44)]

    player = findPlayerByCity(players, 'Funes')

    assert player == players[1]


def test_matchLeftouts():
    # Testeo el matcheo de la gente que quedó sola en las ciudades

    leftoutPlayer = Player('El Peluca', 'La Quiaca', 45)

    leftout = [Player('Juan', 'Rosario', 20), Player(
        'Maria', 'Buenos Aires', 69), leftoutPlayer]

    cities = {
        'Rosario': {
            'neighbor': [
                (
                    'Buenos Aires', 21
                )
            ],
            'players': [],
        },
        'Buenos Aires': {
            'neighbor': [
                (
                    'Rosario', 21
                )
            ],
            'players': [],
        },
        'La Quiaca': {
            'neighbor': [
            ],
            'players': [],
        }
    }

    output = create_test_output()

    matchLeftouts(cities, leftout, output)

    assert leftout == []
    assert len(cities['Rosario']['players']) == 1 or len(
        cities['Buenos Aires']['players']) == 1
    assert cities['La Quiaca']['players'] == [leftoutPlayer]
