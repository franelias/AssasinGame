# import collections

# Player = collections.namedtuple('Player', 'name city age')
class Player:
    def __init__(self, name: str,  city: str, age: int):
        self.name = name
        self.city = city
        self.age = age
