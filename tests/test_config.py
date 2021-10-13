from src.player import Player
from src.config.config import loadPlayersFromFile, loadCitiesFromFile


def players_list(city: str):
    players = [
        Player('Juan', city, 20),
        Player('Juana', city, 40),
        Player('Juanita', city, 60)
    ]

    return players


def test_loadPlayersFromFile():
    cities = {}
    loadPlayersFromFile(cities, '../tests/data/jugadores.txt')

    assert len(cities['Rosario']['adultPlayers']) == 1
    assert len(cities['Rosario']['minorPlayers']) == 1
    assert len(cities['Santa Fe']['adultPlayers']) == 2
    assert len(cities['Santa Fe']['minorPlayers']) == 1


def test_loadCitiesFromFile():
    cities = {
        'Rosario': {
            'neighbor': [],
            'players': players_list('Rosario'),
        },

        'CABA': {
            'neighbor': [],
            'players': players_list('CABA')
        },

        'Santa Fe': {
            'neighbor': [],
            'players': players_list('Santa Fe')
        }
    }
    loadCitiesFromFile(cities, 500, '../tests/data/distancias.txt')

    assert cities['Rosario']['neighbor'] == [('CABA', '299.9')]
    assert cities['Santa Fe']['neighbor'] == [('CABA', '468.5')]
    assert cities['CABA']['neighbor'] == [
        ('Rosario', '299.9'), ('Santa Fe', '468.5')]
