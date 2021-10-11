from src.config.cities_process import adjustNeighbor


def test_AdjustNeighbor():
    # Testea que las listas de jugadores no se modifiquen

    testDict = {
        'Rosario': {
            'neighbor': [
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
