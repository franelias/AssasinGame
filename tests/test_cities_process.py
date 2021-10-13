
import sys
sys.path.append("/src")
from src.config.cities_process import adjustNeighbor


def test_AdjustNeighbor():
    # Testea que las listas de jugadores no se modifiquen y que se ordenen los vecinos de Rosario

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
            'adultPlayers': [
                "lola",
                "juana",
                "fernando"
            ],
            'minorPlayers': [
                "mirtha",
                "el peluca"
            ]
        }
    }

    expectedResult = {
        'Rosario': {
            'neighbor': [
                (
                    'Santa Fe', 100
                ),
                (
                    'CABA', 400
                )
            ],
            'adultPlayers': [
                "lola",
                "juana",
                "fernando"
            ],
            'minorPlayers': [
                "mirtha",
                "el peluca"
            ]
        }
    }

    adjustNeighbor(testDict)

    assert testDict == expectedResult
