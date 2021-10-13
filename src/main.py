import sys
import services.assasin_game as AssasinGame
import config.config as Config
import config.cities_process as CitiesProcess


def main():
    cities = dict()
    playersFile = sys.argv[-2]
    distancesFile = sys.argv[-1]

    maxDistance = Config.inputMaxDistance()

    Config.loadPlayersFromFile(cities, playersFile)
    Config.loadCitiesFromFile(cities, maxDistance, distancesFile)

    CitiesProcess.adjustNeighbor(cities)

    with open('./output.txt', "w+", encoding="utf-8") as output:
        output.write('Juego de mayores: \n')
        for city in cities:
            cities[city]["players"] = cities[city].pop("adultPlayers")

        AssasinGame.start(cities, output)

        output.write('Juego de menores: \n')

        for city in cities:
            cities[city]["players"] = cities[city].pop("minorPlayers")

        AssasinGame.start(cities, output)


if __name__ == "__main__":
    main()
