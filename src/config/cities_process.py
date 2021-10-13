from config.config import Cities

# Función que toma una estructura de datos de tipo Cities y ordena los vecinos de las
# ciudades por distancia de menor a mayor.
# adjustNeighbor: Cities -> None


def adjustNeighbor(cities: Cities):
    for city in cities:
        cities[city]["neighbor"] = sorted(
            cities[city]["neighbor"], key=lambda k: k[1])
