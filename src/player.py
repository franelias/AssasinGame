# Estructura para representar a cada jugador, la cual contiene el nombre, la ciudad y la edad del mismo
class Player:
    def __init__(self, name: str,  city: str, age: int):
        self.name = name
        self.city = city
        self.age = age
