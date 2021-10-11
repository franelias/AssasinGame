from typing import List
from src.player import Player
from src.services.assasin_game import canPlay, fight, findPlayerByCity, makeFights, managePlayers, matchLeftouts


def test_fight():
    Player1 = Player('Juan', 'Rosario', 20)
    Player2 = Player('Maria', 'Funes', 69)

    result = fight([Player1, Player2])

    assert len(result) == 2


def test_canPlay():
    testDict = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                ),
                (
                    'Santa Fe', 100
                )
            ],
            'players': [
                "lola",
                "juana",
                "fernando"
            ],
        }
    }

    testDict2 = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                ),
                (
                    'Santa Fe', 100
                )
            ],
            'players': [
                "lola",
                "juana",
                "fernando"
            ],
        }
    }

    bool1 = canPlay(testDict)
    bool2 = canPlay(testDict2)

    assert bool1 and (not bool2)


def test_managePlayers():
    testDict = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                ),
                (
                    'Santa Fe', 100
                )
            ],
            'players': [
                Player('Juan', 'Rosario', 20),
                Player('Juana', 'Rosario', 40),
                Player('Juanita', 'Rosario', 60)
            ],
        }
    }

    with open('./data_test', 'w+') as output:
        result = managePlayers(testDict, output)

    assert type(result) == List[Player]


def test_makeFights():
    testDict = {
        'Rosario': {
            'neighbor': [
                (
                    'CABA', 400
                ),
                (
                    'Santa Fe', 100
                )
            ],
            'players': [
                Player('Juan', 'Rosario', 20),
                Player('Juana', 'Rosario', 40),
                Player('Juanita', 'Rosario', 60)
            ],
        }
    }

    with open('./data_test', 'w+') as output:
        result = makeFights(output)

    assert type(result) == List[Player]


def test_findPlayerByCity():
    players = [Player('Juan', 'Rosario', 20), Player(
        'Maria', 'Funes', 69), Player('Maria', 'Sante Fe', 44)]

    player = findPlayerByCity(players, 'Funes')

    assert player == Player('Maria', 'Funes', 69)


def test_matchLeftouts():
    players = [Player('Juan', 'Rosario', 20), Player(
        'Maria', 'Funes', 69), Player('Maria', 'Sante Fe', 44)]

    cities = {
        'Rosario': {
            'neighbor': [
                (
                    'Buenos Aires', 21
                )
            ],
            'players': [
                Player('Juana', 'Rosario', 40),
            ],
        },
        'Buenos Aires': {
            'neighbor': [
                (
                    'Rosario', 21
                )
            ],
            'players': [
                Player('Juanita', 'Buenos Aires', 60),
            ],
        }
    }

    with open('./data_test', 'w+') as output:
        result = matchLeftouts(output)

    assert result == []
