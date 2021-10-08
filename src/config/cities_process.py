def adjustNeighbor(cities):
    for city in cities:
        cities[city]["neighbor"] = sorted(
            cities[city]["neighbor"], key=lambda k: k[1])
